from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Place(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.name

  # def get_absolute_url(self):
  #   return reverse('places_detail', kwargs={'place_id': self.id})