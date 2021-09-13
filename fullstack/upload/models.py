from datetime import datetime
from django.db import models
from django.contrib.auth.models import User

# User do Django


class Residence(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField()


class ResidenceImage(models.Model):
    residence = models.ForeignKey(Residence, on_delete=models.DO_NOTHING)
    image = models.ImageField()


class Contract(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    residence = models.ForeignKey(Residence, on_delete=models.DO_NOTHING)
    contract = models.FileField(upload_to='media/contracts/')
    residence_value = models.DecimalField(max_digits=10, decimal_places=2)
    rented_at = models.DateField()
    closed_at = models.DateField()
    updated_at = models.DateField(datetime.now())
