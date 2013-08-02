
from django.conf.urls import patterns, url
from django.views.generic import View

urlpatterns = patterns(
    '',
    url('', View.as_view()),
)
