from django.db import models

# Create your models here.
class User(models.Model):
    userId = models.AutoField(default=0)
    displayName = models.CharField(max_length = 30)
    fbEmail = models.EmailField(max_length = 254)
    phoneNumber = models.CharField(max_length = 10)

    location_lat = models.DecimalField(max_digits = 12, decimal_places = 9)
    location_long = models.DecimalField(max_digits = 12, decimal_places = 9)

class Friend(models.Model):
    #we may choose to either keep twice as many records in the database, or to query the database twice as needed
    firstUser = models.ForeignKey(User)
    secondUser = models.ForeignKey(User)