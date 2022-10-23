from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

VISITED = (
  ('1', 'Visited'),
  ('2', 'Not Visited'),
  ('3', 'Planing To Visit')
)

class Place(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('detail', kwargs={'place_id': self.id})

class Visit(models.Model):
  date = models.DateField('visiting date')
  visited = models.CharField(
    max_length=1,
    choices=VISITED,
    default=VISITED[0][0]
  )

  place = models.ForeignKey(Place, on_delete=models.CASCADE)
  def __str__(self):
    return f"{self.get_visited_display()} on {self.date}"  

  class Meta:
    ordering = ['-date'] 