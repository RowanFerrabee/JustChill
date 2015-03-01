from django.db import models

# Create your models here.
class User(models.Model):
 #   userID = models.AutoField(max_length=10)
    fbToken = models.CharField(max_length=100)
    nick = models.CharField(max_length=30)

class Chill(models.Model):
    user = models.ForeignKey('User')
    start = models.DateTimeField()
    end = models.DateTimeField()
    longitude = models.DecimalField(max_digits=20, decimal_places=14)
    latitude = models.DecimalField(max_digits=20, decimal_places=14)