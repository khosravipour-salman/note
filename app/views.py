from django.shortcuts import render
from app.models import Note


def note_list(request):
    obj_list = Note.objects.all()
    return render(request, 'app/list.html', {"list": obj_list})
