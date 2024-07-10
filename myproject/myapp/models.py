from django.db import models

# Create your models here.

# Introduction to models (Basics)
# class Feature():
    # id: int
    # name: str
    # details: str
    # is_true: bool




# Django admin Panel and Manipulation of database
class Features(models.Model):
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=200)

# User registration