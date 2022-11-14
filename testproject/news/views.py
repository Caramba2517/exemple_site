from django.views.generic import ListView, DetailView
from .models import Post


# Create your views here.


class PostList(ListView):
    queryset = Post.objects.all().order_by('-time_create')
    template_name = 'news.html'
    context_object_name = 'posts'

class PostDetail(DetailView):
    model = Post
    template_name = 'news_detail.html'
    context_object_name = 'post_detail'