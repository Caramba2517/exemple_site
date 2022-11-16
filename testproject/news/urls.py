from django.urls import path
from .views import PostList, PostDetail, create_news, PostUpdate, PostDelete

urlpatterns = [
    path('', PostList.as_view(), name='posts'),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('create/', create_news, name='create_news'),
    path('<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='product_delete'),
    path('search/', PostList.as_view(), name='search'),

]
