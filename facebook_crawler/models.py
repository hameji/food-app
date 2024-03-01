from django.db import models
from django.conf import settings

class Link(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=1000, null=True, blank=True)
    address = models.CharField(max_length=1000, null=True, blank=True)

class Keyword(models.Model):
    def __str__(self):
        return self.words
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    word = models.CharField(max_length=50)