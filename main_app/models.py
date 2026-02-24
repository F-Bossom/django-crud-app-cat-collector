# This has instructions on how to be a django model
from django.db import models
from django.urls import reverse

# we make a new class and inherit all those django model instructions
class Cat(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()

    def __str__(self):
        return f"A Cat named {self.name} that is {self.age} years old."
    
    def get_absolute_url(self):
        return reverse('cat-detail', kwargs={'pk': self.id})