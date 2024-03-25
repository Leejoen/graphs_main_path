from .models import Count
from .models import Edges
from .models import Names
from django.forms import ModelForm, NumberInput, TextInput,CheckboxInput, RadioSelect

class CountForm(ModelForm):
    class Meta:
        model = Count
        fields = ['count']

        widgets = {
            'count': NumberInput(attrs={
                'type': 'range',
                'min': '1',
                'max': '20',
                'value': '5',
                'step': '1',
                'list': 'tickmarks'
            })
        }

class EdgesForm(ModelForm):
    class Meta:
        model = Edges
        fields = ['out', 'to', 'weight']

        widgets = {

        }

class NamesForm(ModelForm):
    class Meta:
        model = Names
        fields = ['num', 'name', 'dangerous']

        widgets = {
            'num': NumberInput(attrs={

            }),

            'name': TextInput(attrs={
                'type': 'text',
                'placeholder': 'Новое название',
                'class': 'name_change'
            }),

            'dangerous': RadioSelect(
                attrs={
                'type': 'radio',
                'name': 'dangerous'
                },
                choices={'True': 'Да', 'False': 'Нет'})
        }
