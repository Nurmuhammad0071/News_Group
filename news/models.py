from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    eamil = models.EmailField(max_length=250)
    age = models.IntegerField()
