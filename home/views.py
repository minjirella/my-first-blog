from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    msg = 'My Message_jimin'
    return render(request, 'home/index.html', {'message' : msg})


def post_list(request):
    return render(request, 'home/post_list.html', {})
