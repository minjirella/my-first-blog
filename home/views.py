from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .models import Post

# Create your views here.
def index(request):
    msg = 'My Message_jimin'
    return render(request, 'home/index.html', {'message' : msg})


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'home/post_list.html', {'posts': posts})
