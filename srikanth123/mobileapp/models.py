from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    active = models.BooleanField(default=False)
    created_on = models.DateTimeField()
    last_logged_in = models.DateTimeField()

class Anurup(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    active = models.BooleanField(default=False)


class Anand(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    active = models.BooleanField(default=False)
class Telsuko(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    active = models.BooleanField(default=False)

