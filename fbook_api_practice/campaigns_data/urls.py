from django.conf.urls import url
from . import views

app_name = 'fbook_campaigns'
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^data/$', views.data, name="data"),
]
