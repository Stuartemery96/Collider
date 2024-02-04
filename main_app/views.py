from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Event, Collide
from .forms import CustomSignupForm

# Create your views here.
def home(request):
    return render(request, 'home.html')


@login_required
def events_index(request):
    events = Event.objects.filter(creator=request.user)
    return render(request, 'events/index.html', { 'events': events })


@login_required
def events_detail(request, event_id):
    event = Event.objects.get(id=event_id)
    collides = Collide.objects.filter(event=event)
    return render(request, 'events/detail.html', { 'event': event, 'collides': collides })


class EventCreate(LoginRequiredMixin, CreateView):
    model = Event
    fields = ['title', 'date', 'category', 'description', 'details']
    
    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)
    
    
class CollideCreate(LoginRequiredMixin, CreateView):
    model = Collide
    fields = ['location', 'time', 'details']
    
    def form_valid(self, form):
        form.instance.host = self.request.user
        event_id = self.kwargs.get('event_id')
        event = get_object_or_404(Event, pk=event_id)
        form.instance.event = event
        return super().form_valid(form)


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = CustomSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid Sign Up - Try Again'
    form = CustomSignupForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)
