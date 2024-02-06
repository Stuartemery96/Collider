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
class Event(models.Model):
  creator = models.ForeignKey(User, on_delete=models.CASCADE)
  title = models.CharField(max_length=100)
  date = models.DateField('Event Date')
  category = models.CharField(max_length= 100)
  description = models.CharField(max_length=125, help_text='A short description of the event')
  details = models.TextField(max_length=750)
  
  def save(self, *args, **kwargs):
    self.title = self.title.upper()
    self.category = self.category.upper()
    super().save(*args, **kwargs)
  
  def __str__(self):
    return f'{self.title}'
  
  def get_absolute_url(self):
    return reverse('events_detail', kwargs={'event_id': self.id})


class Collide(models.Model):
  host = models.ForeignKey(User, on_delete=models.CASCADE)
  location = models.CharField(max_length=100)
  time = models.TimeField('Event Time')
  details = models.TextField(max_length=400)
  event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='collides')

  def get_absolute_url(self):
    return reverse('events_detail', kwargs={'event_id': self.event_id})


class Rsvp(models.Model):
  attendee = models.ForeignKey(User, on_delete=models.CASCADE)
  collide = models.ForeignKey(Collide, on_delete=models.CASCADE)



class Rating(models.Model):
  rated_user = models.ForeignKey(User, on_delete=models.CASCADE)
  rating_user = models.ForeignKey(User,related_name='rating_user', on_delete=models.CASCADE)
  rating = models.IntegerField(
    choices=RATES,
    default=RATES[4][0])