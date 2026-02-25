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
    
MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner'),
)
    
class Feeding(models.Model):
    date = models.DateField("Feeding Date")
    meal = models.CharField(
        verbose_name="Meal:",
        max_length=1,
        choices=MEALS, # this works like a enum and provides choices
        default=MEALS[0][0] 
        ) # (B,L,D Breakfast, Lunch, Dinner)
    
    # setting up a relationship - one to many
    # we can use the models.ForeignKey(Table_To_Ref, on_delete=models.cascade
    # models.CASCADE tells django if the parent cat is deleted, 
    # then delete all the related feedings to that cat
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE, related_name='feedings')
    # this Feeding will show up under the cat on feeding_set  or modelName_set

    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"