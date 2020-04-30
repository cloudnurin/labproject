from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'fullcalendar'
urlpatterns = [
    # path('add_event/', views.add_event, name='add_event'),
    # path('calendar/', views.calendar, name='calendar'),
    # path('update/', views.update, name='update'),
    # path('remove/', views.remove, name='remove'),
    url('^calendar', views.calendar, name='calendar'),
    url('^add_event$', views.add_event, name='add_event'),
    url('^update$', views.update, name='update'),
    url('^remove', views.remove, name='remove'),
]
