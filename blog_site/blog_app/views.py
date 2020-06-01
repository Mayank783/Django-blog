from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post 

# Create your views here.

def home(Request):
    context={
        'posts': Post.objects.all() 
    }
    return render(Request ,"home.html",context)
class PostListView(ListView):
    model=Post
    template_name='home.html'    #<app>/<model>_<viewtype>.html
    context_object_name='posts'
    ordering=['-date_posted']

class PostDetailView(DetailView):
    model=Post


def about(Request):
    return render(Request,"about.html",{'title':'About'})