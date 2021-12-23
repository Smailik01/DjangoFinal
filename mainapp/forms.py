from django import forms
from .models import *


class newMessage(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('name', 'email', 'mtext')
        labels = {'name': 'Your Name', 'email': 'Email', 'mtext':'Message'}
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your FullName...'}),
            'email' : forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Enter your Email...'}),
            'mtext' : forms.Textarea(attrs={ 'class':'form-control', 'placeholder':'Message...'})
        }

class studentRegistration(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('name', 'surname', 'username', 'email', 'phone')
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your First Name...'}),
            'surname' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your Last Name...'}),
            'username' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your Username...'}),
            'email' : forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Enter your Email...'}),
            'phone' : forms.NumberInput(attrs={ 'class':'form-control', 'placeholder':'Enter your Phone Number...'})
        }