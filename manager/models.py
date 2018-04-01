from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

from . import manufacturers 

class ModelTrain(models.Model):
    TRACTION_TYPES = (
        ("Diesel", "Diesel"),
        ("Petrol", "Petrol"),
        ("Steam", "Steam"),
        ("Electric", "Electric"),
    )

    SCALES = (
        ("OO", "OO"),
        ("HO", "HO"),
        ("TT", "TT"),
        ("N", "N"),
    )

    manufacturer = models.CharField(max_length=100, choices=manufacturers.MANUFACTURERS)

    name = models.CharField(max_length=30)

    model_class = models.CharField(max_length=30)

    traction = models.CharField(max_length=10, choices=TRACTION_TYPES)

    scale = models.CharField(max_length=2, choices=SCALES)

    era = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(9)])

    def __str__(self):
        return self.name

class Collection(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=30)

    description = models.CharField(max_length=300)

    trains = models.ManyToManyField(ModelTrain)

    def __str__(self):
        return self.name