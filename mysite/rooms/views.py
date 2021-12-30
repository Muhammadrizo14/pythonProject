from django.shortcuts import render
from django.views.generic import ListView
from .models import *


# Create your views here.
class HomeNews(ListView):
    model = Rooms
    context_object_name = 'room'
    template_name = 'index.html'
    ordering = 'is_published'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home'
        context['subtitle'] = '<A>code'
        return context