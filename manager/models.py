from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse

from . import manufacturers


class ModelTrain(models.Model):
    TRACTION_TYPES = (
        ('Diesel', 'Diesel'),
        ('Petrol', 'Petrol'),
        ('Steam', 'Steam'),
        ('Electric', 'Electric'),
    )

    SCALES = (
        ('OO', 'OO'),
        ('HO', 'HO'),
        ('TT', 'TT'),
        ('N', 'N'),
    )

    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=30)

    manufacturer = models.CharField(
        max_length=100, choices=manufacturers.MANUFACTURERS,
        default=manufacturers.MANUFACTURERS[0][0])

    model_class = models.CharField(max_length=30)

    traction = models.CharField(
        max_length=10, choices=TRACTION_TYPES, default=TRACTION_TYPES[0][0])

    scale = models.CharField(
        max_length=2, choices=SCALES, default=SCALES[0][0])

    era = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(9)])

    def get_absolute_url(self):
        return reverse('model-train-detail', args=[str(self.id)])

    def __str__(self):
        return self.name


class Collection(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=30)

    description = models.CharField(max_length=300)

    trains = models.ManyToManyField(ModelTrain, through='CollectionTrain', blank=True)

    def get_absolute_url(self):
        return reverse('collection-detail', args=[str(self.id)])

    def __str__(self):
        return self.name


class CollectionTrain(models.Model):
    trains = models.ForeignKey(ModelTrain, on_delete=models.CASCADE)

    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
