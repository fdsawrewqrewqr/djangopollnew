from django.conf.urls import patterns,url
from polls import views

#urlpatterns=patterns('',url(r'^$',views.index,name='index'))
urlpatterns=patterns('',url(r'^$', views.index, name='index'),)