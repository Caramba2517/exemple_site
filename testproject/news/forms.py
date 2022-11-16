from django.forms import ModelForm, BooleanField
from .models import Post


class PostForm(ModelForm):
    check_box = BooleanField(label='Готово')

    class Meta:
        model = Post
        fields = ['status', 'headline', 'content', 'author_post', 'categories', 'check_box']
