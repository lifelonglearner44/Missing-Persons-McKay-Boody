from django.db import models
from datetime import datetime

# Create your models here.

class Person (models.Model):
    date_missing = models.DateField(default=datetime.today)
    last_name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    age_missing = models.IntegerField()
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=2)
    gender = models.CharField(max_length=1)
    race = models.CharField(max_length=20)

    def __str__(self):
        return(self.last_name)
