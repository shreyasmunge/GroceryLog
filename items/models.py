from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class GroceryItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    description = models.TextField(blank=True)



    def __str__(self):
        return self.name
    
