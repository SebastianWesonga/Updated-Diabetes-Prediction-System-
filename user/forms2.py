from django import forms
from django.contrib.auth.models import User
from django.forms import fields
from django.forms.fields import CharField
from django.forms.widgets import PasswordInput, TextInput, RadioSelect
from .models import Profile

class LoginForm(forms.Form):
  username = forms.CharField(widget=forms.TextInput(attrs={'type':"username",
                    "minlength":"4",
                    "autocomplete":"off",
                    "required":"True"}), label='Username:')
  password = forms.CharField(widget=forms.TextInput(attrs={'type':"password","minlength":"4",
                    "autocomplete":"off",
                    "required":"True"}), label='Password:')


class UserRegistrationForm(forms.ModelForm):
  password = CharField(label="Password", widget=forms.PasswordInput(attrs={
    'type':"password","minlength":"4",
    "class":"input-field",
    "autocomplete":"off",
    "required":"True"
  }))
  password2 = CharField(label="Repeat_Password", widget=forms.PasswordInput(attrs={
    'type':"password","minlength":"4",
    "class":"input-field",
    "autocomplete":"off",
    "required":"True"
  }))
  GENDER_CHOICES = [
          ('M', 'Male'),
          ('F', 'Female'),
          ]

  gender = forms.ChoiceField(label="gender", choices = GENDER_CHOICES, widget=forms.RadioSelect(attrs={
    'type':"password",
    "required":"True"
  }))

  telephone = CharField(label="telephone", widget=forms.TextInput(attrs={
    'type':"tel","minlength":"10",
    "autocomplete":"off",
    "required":"True"
  }))

  address = CharField(label="address", widget=forms.TextInput(attrs={
    'type':"text","minlength":"4",
    "autocomplete":"off",
    "required":"True"
  }))

  date_of_birth = forms.DateField(label="date_of_birth",
          widget=forms.NumberInput(attrs={
    'type':"date",
    "required":"True"
  }))


  class Meta:
    model = User
    fields ={'username', 'first_name','last_name', 'email'}
    widgets = {
      'username': TextInput(attrs={"type":"username",
                    "minlength":"4",
                    "autocomplete":"off",
                    "required":"True"

      }),

      'first_name': TextInput(attrs={"type":"username",
                    "minlength":"4",
                    "class":"input-field",
                    "autocomplete":"off",
                    "required":"True"

      }),
      'last_name': TextInput(attrs={"type":"username",
                    "minlength":"4",
                    "class":"input-field",
                    "autocomplete":"off",
                    "required":"True"

      }),
      'email': TextInput(attrs={"type":"email",
                    "minlength":"4",
                    "class":"input-field",
                    "autocomplete":"off",
                    "required":"True"

      }),
    }
  def clean_password2(self):
    cd = self.cleaned_data
    if cd['password'] != cd['password2']:
      raise forms.ValidationError("Passwords do not match!")
    return cd['password2']


