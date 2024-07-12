from django.db import models

class Person(models.Model):
    account_number = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    amount=models.FloatField()