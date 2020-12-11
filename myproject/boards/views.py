from django.shortcuts import render, get_object_or_404

# Create your views here.


from django.http import HttpResponse
from .models import Board
from .models import BondFund


def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})


def bond(request):
    bonds = BondFund.objects.all()
    return render(request, 'bond.html', {'bond': bonds})
