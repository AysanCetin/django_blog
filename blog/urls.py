from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    
#    path('', views.post_list, name='postlist'),

    path('', views.PostListView.as_view(), name='postlist'),
    path('(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/', views.post_detail, name='post_detail'),

]