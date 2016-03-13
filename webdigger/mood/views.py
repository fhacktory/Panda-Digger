# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.views import generic

import mpvdigger


class IndexView(generic.TemplateView):
    template_name = 'mood/index.html'


def new(request, from_id):
    entries = []
    for entry in mpvdigger.mpv.playlist[int(from_id):]:
        entries.append(u'{} - {} - {} - {}'.format(
            entry.artist or u'<em>Pas d\'artiste</em>',
            entry.album or u'<em>Pas d\'album</em>',
            entry.title or u'<em>Pas de titre</em>',
            entry.duration or u'<em>Pas de durée</em>'))
    return JsonResponse({'new': entries})


def pos(request):
    return JsonResponse({'pos': mpvdigger.mpv.pos})


def play(request, index):
    index = int(index)
    if index == mpvdigger.mpv.pos:
        mpvdigger.mpv.stop()
    else:
        mpvdigger.mpv.goto(index)
    return JsonResponse({})
