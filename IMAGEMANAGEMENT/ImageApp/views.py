from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.http import HttpResponse
from .models import Post
from django.views import generic

# Create your views here.

class IndexView(TemplateView):
    template_name = 'post/base.html'

    def get__queryset(self):
       return Post.objects.all()

class DetailView(generic.DetailView):
    model = Post
    template_name = 'post/detail.html'

class ImageView(TemplateView):
    template_name = 'post/imageview.html'