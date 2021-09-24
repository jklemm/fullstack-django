from django.db import models
from django.contrib.auth.models import User


class Room(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.TextField(max_length=1000, null=False)
    value = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    available = models.BooleanField(null=False, default=False)

    def __str__(self):
        return self.name


class RoomImage(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=False)

    def delete(self, *args, **kwargs):
        self.room.delete()
        super().delete(args, **kwargs)


class Contract(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    room = models.ForeignKey(Room, on_delete=models.PROTECT, null=True)
    contract = models.FileField(upload_to='contracts/', null=False)
    residence_value = models.IntegerField(null=False)
    rented_at = models.DateField(null=False)
    closed_at = models.DateField(null=True)
    updated_at = models.DateField(null=True)

    def delete(self, *args, **kwargs):
        self.contract.delete()
        super().delete(args, **kwargs)