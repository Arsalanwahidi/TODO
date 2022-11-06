from django import forms
from django.forms import ModelForm
from .models import TodoList

#Form Goes here

class TodoForm(ModelForm):

    class Meta:
        model = TodoList
        fields =  '__all__'

