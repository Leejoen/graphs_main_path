from django.forms.models import BaseModelForm
from django.shortcuts import render, redirect
from django.template.defaulttags import register
from django.views.generic import UpdateView, CreateView
from .models import Count, Names, Edges
from .forms import CountForm, NamesForm, EdgesForm
from .connect_db import connect

@register.filter
def get_range(value):
    return range(1, value + 1)

@register.filter
def get_pk(path):
    return int(path.replace('/edges/', ''))

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

class UpdName(UpdateView):
    model = Names
    template_name = 'main/upd_name.html'
    context_object_name = 'name'
    form_class = NamesForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        count = Names.objects.all()
        context['count'] = count

        return context
    

class CreateEdges(CreateView):
    model = Edges
    template_name = 'main/edges.html'
    
    form_class = EdgesForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        count = Names.objects.all()
        context['count'] = count

        return context


def visual(request):
    return render(request, 'main/visual.html')
