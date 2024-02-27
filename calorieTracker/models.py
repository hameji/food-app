from django.db import models

class Food(models.Model):

    def __str__(self):
        return self.name
    
    name = models.CharField(max_length=100)
    carbs = models.FloatField()
    protein = models.FloatField()
    fats = models.FloatField()
    calories = models.IntegerField()    

