from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.http import HttpResponse
from .models import Events
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.cache import cache_page
import json
from django.utils import timezone
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
     event = Events.objects.create(
              title = title,
              start = timezone.now(),
              end = timezone.now()
         )
     event.save()
     data = {}
     return JsonResponse(data)

def update(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    id = request.GET.get("id", None)
    event = Events.objects.get(id=id)
    event.start = start
    event.end = end
    event.name = title
    event.save()
    data = {}
    return JsonResponse(data)


def remove(request):
    id = request.GET.get("id", None)
    event = Events.objects.get(id=id)
    event.delete()
    data = {}
    return JsonResponse(data)