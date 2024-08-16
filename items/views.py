from django.shortcuts import render,get_object_or_404,redirect
from .models import GroceryItem
from .forms import GroceryItemForm,SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required

@login_required
def item_list(request):
    items = GroceryItem.objects.filter(user=request.user)
    return render(request,'items/item_list.html',{'items':items})

@login_required
def item_detail(request,pk):
    item = get_object_or_404(GroceryItem,pk=pk)
    return render(request,'items/item_detail.html',{'item':item})

@login_required
def item_create(request):
    if request.method == 'POST':
        form = GroceryItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            form.save()
            return redirect('item_list')
    else:
        form = GroceryItemForm()
    return render(request,'items/item_form.html',{'form':form})

@login_required
def item_update(request,pk):
    item = get_object_or_404(GroceryItem,pk=pk)
    if request.method == 'POST':
        form = GroceryItemForm(request.POST,instance=item)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = GroceryItemForm(instance=item)
    return render(request,'items/item_form.html',{'form':form})

@login_required
def item_delete(request,pk):
    item = get_object_or_404(GroceryItem,pk=pk)
    if request.method =='POST':
        item.delete()
        return redirect('item_list')
    return render(request,'items/item_confirm_delete.html',{'item':item})

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password =form.cleaned_data.get('password')
            user = authenticate(username=username,password=raw_password)
            login(request,user)
            return redirect('item_list')
    else:
        form = SignUpForm()
    return render(request,'items/signup.html',{'form':form})
    

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('item_list')
    else:
        form = AuthenticationForm()
    return render(request,'items/login.html',{'form':form})
        
def logout_view(request):
    logout(request)
    return redirect('login')






