from collections.abc import Mapping
from typing import Any
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from django.shortcuts import get_object_or_404
from django.forms import EmailField, CharField, ModelForm
from .models import Rsvp, Collide, Rating, Event


class CustomSignupForm(UserCreationForm):
  email = EmailField(max_length=150, help_text='Required')
  first_name = CharField(max_length=150, help_text='Required')
  last_name = CharField(max_length=150, help_text='Required')
  
  class Meta:
    model = User
    fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']


class RsvpForm(ModelForm):
  class Meta:
    model = Rsvp
    fields = []
    
  def __init__(self, *args, collide_id=None, request=None, **kwargs):
      self.collide_id = collide_id
      self.request = request
      super().__init__(*args, **kwargs)
      print(f"Request: {self.request}")

  def save(self, commit=True):
      rsvp = super().save(commit=False)
      rsvp.attendee = self.request.user
      rsvp.collide = Collide.objects.get(pk=self.collide_id)
      if commit:
          rsvp.save()
      return rsvp
  

class RatingForm(ModelForm):
  class Meta: 
    model = Rating
    fields = ['rating']
    
    
class EventForm(ModelForm):
  class Meta:
    model = Event
    fields = ['title', 'date', 'category', 'description', 'details']