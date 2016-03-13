from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^new/(?P<from_id>[0-9]+)$', views.new, name='new'),
    url(r'^pos$', views.pos, name='pos'),
    url(r'^play/(?P<index>[0-9]+)$', views.play, name='play'),
]
