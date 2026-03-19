from django.db import models

# Create your models here.
class Location(models.Model):
    name:str = models.CharField(null=False, blank=False, unique=True)
    detail:str = models.TextField()
    
    def __str__(self):
        return f""