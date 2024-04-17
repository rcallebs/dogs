from django.db import models
from django.urls import reverse

MEALS = (
    ('B', 'Breakfast'),
    ('D', 'Dinner'),
    ('S', 'Snack')
)

class Trait(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('traits_detail', kwargs={'pk': self.id})

# Create your models here.
class Dog(models.Model):
    name = models.CharField(max_length=50)
    breed =  models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    age = models.IntegerField()
    traits = models.ManyToManyField(Trait)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'dog_id': self.id})
    
class Feeding(models.Model):
    date = models.DateField('feeding date')
    meal = models.CharField(
        max_length=1,
        choices=MEALS,
        # default to a snack
        default=MEALS[2][0]
        )
    # Create a dog_id foreign key
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']