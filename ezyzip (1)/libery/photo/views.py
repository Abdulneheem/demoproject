from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.



def cr7(request):
    return render(request, 'cr7.html',{'n':'john',  'j': 'jaik'})

def messi(request):
    return render(request, 'messi.html',{'n':'john',  'j': 'jaik'})