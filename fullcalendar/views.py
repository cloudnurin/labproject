from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.http import HttpResponse
from .models import Events
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.cache import cache_page
import json
import datetime

# Create your views here.

def calendar(request):
    all_events = Events.objects.all()

    context = { 
        "events":all_events,
    }
    return render(request,'fullcalendar/calendar.html',context)

def add_event(request):
     title = request.GET.get("title", None)
     start = request.GET.get("start", None)
     end = request.GET.get("end", None)
     event = Events(title=str(title), start=start, end=end)
     event.save()
     data = {}
     return JsonResponse(data)

def update(request):
    id = request.GET.get("id", None)
    print(id)
    event = Events.objects.get(id=id)
    title = request.GET.get("title", None)
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    event.start = start
    event.end = end
    event.title = title
    event.save()
    data = {}
    return JsonResponse(data)

def remove(request):
    id = request.GET.get("id", None)
    event = Events.objects.get(id=id)
    event.delete()
    data = {}
    return JsonResponse(data)