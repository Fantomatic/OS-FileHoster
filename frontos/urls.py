from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='index.html'), name="index"),
    # url(r'^$', TemplateView.as_view(template_name='home.html'), name="home"),
    # url(r'^frontks', include('frontos.apps.frontks.urls', namespace="frontks")),
)
