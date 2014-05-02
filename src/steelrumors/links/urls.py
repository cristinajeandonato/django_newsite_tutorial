from django.conf.urls import patterns, url

from links import views

urlpatterns = patterns('',
    # ex:/polls/
    url(r'^$', views.LinkListView.as_view(), name='index'),
    
    
)
