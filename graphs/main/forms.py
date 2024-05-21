from .models import Count
from .models import Edges
from .models import Names
from django.forms import ModelForm, NumberInput, TextInput, CheckboxInput, RadioSelect, Select

#импорт класса мультиформы (MultiFormsView - представление для отображения нескольких форм и отображения ответа шаблона, BaseMultipleFormsView - "базовый" класс для отображения нескольких форм).
from multiform import MultiFormMixin, ProcessMultipleFormsView, BaseMultipleFormsView, MultiFormsView

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
            'out': NumberInput(attrs={
                'value': 1
            }),

            'to': Select(attrs={
                
            }),

            'weight': NumberInput(attrs={
                'min': 0,
                'max': 1,
                'value': 0,
                'step': .1
            })
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
