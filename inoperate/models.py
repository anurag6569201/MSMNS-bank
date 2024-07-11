from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    account_number = models.CharField(max_length=20)
    amount=models.IntegerField()