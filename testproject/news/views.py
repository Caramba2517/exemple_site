
from django.views.generic import ListView
from .models import *
# Create your views here.

class PostList(ListView):
    model = Post
    ordering = 'time_create'
    template_name = 'news_page.html'
    context_object_name = 'news_page'

