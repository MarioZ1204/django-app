import datetime
from django.db import models

# Create your models here.
#usamos models.Model para usar los timpos de campos ejemplos variables
class User(models.Model):
    email = models.EmailField(null = True, blank = True) 
    password = models.CharField(null = True, blank = True)
    status = models.BooleanField(default= True)
    created_at = models.DateTimeField(default = datetime.datetime.now()) # blank = true que acaepte valores null
    updated_at = models.DateTimeField(default = datetime.datetime.now())
    deleted_at = models.DateTimeField(null = True, blank = True)

class Person (models.Model):
    firstname = models.CharField(max_length = 20) 
    lastname = models.CharField(max_length = 20)
    age = models.IntegerField()
    ident_number = models.CharField(max_length = 12, blank = True) # blank = true que acaepte valores null
    created_at = models.DateTimeField(default = datetime.datetime.now())
    updated_at = models.DateTimeField(default = datetime.datetime.now())
    deleted_at = models.DateTimeField(null = True, blank = True)
