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
    entries = []
    for entry in mpv.playlist[int(from_id):]:
        entries.append(u'{} - {} - {} - {}'.format(
            entry.artist, entry.album, entry.title, entry.duration))
    return JsonResponse({'new': entries})


def pos(request):
    return JsonResponse({'pos': mpv.pos})


def play(request, index):
    index = int(index)
    if index == mpv.pos:
        mpv.stop()
    else:
        mpv.goto(index)
    return JsonResponse({})
