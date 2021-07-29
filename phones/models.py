from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.deletion import CASCADE

# Create your models here.

class Phone(models.Model):
    name = models.CharField(max_length=64)
    price = models.CharField(max_length=64)
    specifications = models.TextField()
    rating = models.FloatField()
    company = models.ForeignKey(get_user_model(), on_delete=CASCADE)

    def __str__(self):
        return self.name
