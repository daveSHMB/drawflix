from django.conf.urls import patterns, url
from drawflix import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^about/$', views.about, name='about'),
        url(r'^most_recent/$', views.most_recent, name='most_recent'),
        url(r'^trending/$', views.trending, name='trending'),
        url(r'^hall_of_fame/$', views.hall_of_fame, name='hall_of_fame'),
        url(r'^like_drawing/$', views.like_drawing, name='like_drawing'),
        url(r'^add_drawing/$', views.add_drawing, name='add_drawing'),
        url(r'^archive/$', views.archive, name='archive'),
        url(r'^user/$', views.user_drawings, name='user_drawings'),
        )
