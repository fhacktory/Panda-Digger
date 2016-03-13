from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.views import generic
from mpvdigger import Mpv

mpv=Mpv()
mpv.add('poulet')
mpv.add('canard')
mpv.add('dromadaire')


class IndexView(generic.TemplateView):
    template_name = 'mood/index.html'


def new(request, from_id):
    return JsonResponse({'new': mpv.playlist[int(from_id):]})


def pos(request):
    return JsonResponse({'pos': mpv.pos})


def play(request, index):
    mpv.goto(int(index))
    return JsonResponse({})
