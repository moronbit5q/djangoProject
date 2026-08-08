from django.shortcuts import render
from django.views.generic import ListView, DetailView # new
from django.views.generic.edit import CreateView # new

from .models import Post # our databse model post

# Create your views here.

class BlogListView(ListView):
    model = Post
    template_name = 'home.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = '__all__'