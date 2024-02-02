from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import EmailField, CharField


class CustomSignupForm(UserCreationForm):
    # def __init__(self, *args, **kwargs):
    #   super(CustomSignupForm, self).__init__(*args, **kwargs)
    #   self.fields['email'] = EmailField(max_length=150, help_text='Required')
    email = EmailField(max_length=150, help_text='Required')
    first_name = CharField(max_length=150, help_text='Required')
    last_name = CharField(max_length=150, help_text='Required')
    
    class Meta:
      model = User
      fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']

    # def save(self, request):
    #     email = self.cleaned_data.pop('email')
    #     user = super(CustomSignupForm, self).save(request)