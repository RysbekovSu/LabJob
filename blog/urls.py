from django.urls import path
from . import views
urlpatterns = [
    path('post/', views.blog_all, name='post'),
    path('post_detail/<int:id>', views.PostDetail.as_view(), name='detail'),
    path('add-post/', views.PostCreate.as_view(), name='add-post'),
]

