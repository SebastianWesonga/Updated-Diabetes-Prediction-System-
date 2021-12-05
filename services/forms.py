from django import forms
from .models import Service
from django.forms.fields import CharField
from django.forms.widgets import TextInput, NumberInput

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields =('pregnacies', 'glucose', 'blood_pressure', 'skin_thickness',
                'insulin', 'bmi', 'diabetes_pedigree', 'age' )
        widgets = {
                'pregnacies' : NumberInput(attrs={"type":"num",
                    "autocomplete":"off",
                    "required":"false"}),

                'glucose' : TextInput(attrs={"type":"text",
                    "autocomplete":"off",
                    "required":"true"}),

                'blood_pressure' : TextInput(attrs={"type":"text",
                    "autocomplete":"off",
                    "required":"true"}),

                'skin_thickness' : TextInput(attrs={"type":"text",
                    "autocomplete":"off",
                    "required":"true"}),

                'insulin' : TextInput(attrs={"type":"text",
                    "autocomplete":"off",
                    "required":"true"}),

                'bmi' : TextInput(attrs={"type":"text",
                    "autocomplete":"off",
                    "required":"true"}),

                'diabetes_pedigree' : TextInput(attrs={"type":"text",
                    "autocomplete":"off",
                    "required":"true"}),

                'age' : NumberInput(attrs={"type":"num",
                    "autocomplete":"off",
                    "required":"true"}),
                }
