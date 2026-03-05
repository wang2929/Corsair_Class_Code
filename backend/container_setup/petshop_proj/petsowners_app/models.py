from django.db import models

# Create your models here.
class Owner(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField()
    age = models.BigIntegerField()
    number_of_pets = models.BigIntegerField()

class Cat(models.Model):
    id = models.BigIntegerField(primary_key=True)
    breed = models.CharField()
    age = models.BigIntegerField()
    vaccinated = models.BooleanField(default=False)
    description = models.TextField()
    name = models.CharField()
    
class Dog(models.Model):
    id = models.BigIntegerField(primary_key=True)
    age = models.BigIntegerField()
    name = models.CharField()
    vaccinated = models.BooleanField(default=False)
    breed = models.CharField()
    description = models.TextField()
    
class Bird(models.Model):
    id = models.BigIntegerField(primary_key=True)
    age = models.BigIntegerField()
    name = models.CharField()
    vaccinated = models.BooleanField(default=False)
    species = models.CharField()
    description = models.TextField()
    
class ExoticAnimal(models.Model):
    id = models.BigIntegerField(primary_key=True)
    region_of_origin = models.CharField()
    name = models.CharField()
    age = models.BigIntegerField()
    type_of_animal = models.CharField()
    vaccinated = models.BooleanField(default=False)