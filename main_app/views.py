from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .models import Event
from .forms import CustomSignupForm

# Create your views here.
def home(request):
    return render(request, 'home.html')


@login_required
def events_index(request):
    events = Event.objects.filter(user=request.user)
    return render(request, 'events/index.html', { 'events': events })


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
