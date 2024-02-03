from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date, time


RATES = (
  (1, '⭐️'),
  (2, '⭐️⭐️'),
  (3, '⭐️⭐️⭐️'),
  (4, '⭐️⭐️⭐️⭐️'),
  (5, '⭐️⭐️⭐️⭐️⭐️'),
)

# Create your models here.
class Rsvp(models.Model):
  attendee = models.ForeignKey(User, on_delete=models.CASCADE)


class Collides(models.Model):
  host = models.ForeignKey(User, on_delete=models.CASCADE)
  location = models.CharField(max_length=100)
  time = models.TimeField('Event Time')
  details = models.TextField(max_length=400)
  rsvps = models.ForeignKey(Rsvp, on_delete=models.CASCADE)


class Event(models.Model):
  title = models.CharField(max_length=100)
  date = models.DateField('Event Date')
  category = models.CharField(max_length= 100)
  details = models.TextField(max_length=750)
  collides = models.ForeignKey(Collides, on_delete=models.CASCADE)
  
  def __str__(self):
    return f'{self.title}'
  
  def get_absolute_url(self):
    return reverse('event_detail', kwargs={'event_id': self.id})


class Rating(models.Model):
  rated_user = models.ForeignKey(User, on_delete=models.CASCADE)
  rating = models.IntegerField(
    choices=RATES,
    default=RATES[4][0])
  
  def get_rating_display(self):
    return dict(RATES)[self.rating]