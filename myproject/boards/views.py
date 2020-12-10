from django.shortcuts import render, get_object_or_404

# Create your views here.


from django.http import HttpResponse
from .models import Board


def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})
