from django import forms
from .models import Todos

class TodoModelForm(forms.ModelForm):
    class Meta():
        model = Todos
        fields = [ 'task' ]
        labels = {
            'task': '',
        }
        widgets = {
            'task': forms.TextInput(attrs = { 'placeholder': 'Add Task' }),
        }
