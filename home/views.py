from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    msg = 'My Message_jimin'
    return render(request, 'index.html', {'message' : msg})
