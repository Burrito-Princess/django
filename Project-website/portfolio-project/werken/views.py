from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Werken
from django.utils import timezone

# Create your views here.

def home(request):
 werken = Werken.objects
 return render(request, 'werken/werken.html', {'werken': werken})

def detail(request, werken_id):
 werk = get_object_or_404(Werken, pk=werken_id)
 return render(request, 'werken/detail.html', {'werk': werk})