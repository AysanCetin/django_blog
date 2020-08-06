from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [

    path('', views.PostListView.as_view(), name='post_list'),
    path('post_detail/<int:pk>', views.post_detail, name='post_detail'),
    path('post_detail/post_share/<int:pk>', views.post_share, name='post_share'),
]