from django import forms
from .models import GroceryItem
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class GroceryItemForm(forms.ModelForm):
    class Meta:
        model = GroceryItem
        fields = ('name', 'quantity', 'description')

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1')  # Only include username, email, and password1
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
        }
        help_texts = {
            'username': '',  # Remove help text for username
            'email': '',     # Remove help text for email (if any)
            'password1': '', # Remove help text for password1
        }
        error_messages = {
            'password1': {
                'password_too_similar': '',
                'password_too_short': '',
                'password_too_common': '',
                'password_entirely_numeric': '',
            },
        }