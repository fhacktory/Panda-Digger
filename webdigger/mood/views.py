from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views import generic

# Create your views here.
class IndexView(generic.TemplateView):
    template_name = 'mood/index.html'

