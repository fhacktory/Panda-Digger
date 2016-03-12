from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views import generic
from mpvdigger import Mpv

supermpv=Mpv()

# Create your views here.
class IndexView(generic.TemplateView):
    global supermpv
    supermpv.add('poulet')
    supermpv.add('canard')
    supermpv.add('dromadaire')

    template_name = 'mood/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['playlist'] = supermpv.playlist
        return context
