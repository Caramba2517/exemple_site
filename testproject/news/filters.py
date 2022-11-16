from django.forms import DateInput
from django_filters import FilterSet, CharFilter, DateFilter, ModelChoiceFilter
from .models import Post, Author


class PostFilter(FilterSet):
    headline = CharFilter('headline',
                          label='Заголовок содержит:',
                          lookup_expr='icontains', )

    content = CharFilter('content',
                         label='Текст содержит:',
                         lookup_expr='icontains',
                         )

    author_post = ModelChoiceFilter(field_name='author_post',
                                    label='Автор:',
                                    lookup_expr='exact',
                                    queryset=Author.objects.all()
                                    )
    time_create = DateFilter(
        field_name='time_create',
        widget=DateInput(attrs={'type': 'date'}),
        lookup_expr='gt',
        label='Дата публикации:'
    )

    class Meta:
        model = Post
        fields = []
