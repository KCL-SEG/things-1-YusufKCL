from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Things(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=120)
    quantity = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])