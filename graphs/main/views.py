from django.shortcuts import render, redirect
from django.template.defaulttags import register
from django.views. generic import DetailView, ListView
from .models import Count, Names
from .forms import CountForm, NamesForm
from .connect_db import connect

@register.filter
def get_range(value):
    return range(1, value + 1)

def index(request):
    if request.method == 'POST':
        form = CountForm(request.POST)
        form.save()
        connect()
        return redirect('params')

    form = CountForm()

    data = {
        'form': form
    }

    return render(request, 'main/index.html', data)

def params(request):
    count = Names.objects.all()

    if request.method == 'POST':
        form_name = NamesForm(request.POST)
        form_name.save()

    form_name = NamesForm()

    data = {
        'form_name': form_name,
        'count': count
    }

    return render(request, 'main/params.html', data)

class Param(DetailView):
    model = Names
    template_name = 'main/param.html'
    context_object_name = 'name'

def visual(request):
    return render(request, 'main/visual.html')
