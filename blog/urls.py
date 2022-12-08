from django.urls import path
from . import views
app_name = 'users'
urlpatterns = [
    path('registration/', views.Registration.as_view(), name='registration'),
    path('post/', views.blog_all, name='post'),
    path('post_detail/<int:id>', views.PostDetail.as_view(), name='detail'),
    path('add-post/', views.PostCreate.as_view(), name='add-post'),
    path('login/', views.NewLoginForm.as_view(), name='login'),
    path('users/', views.UserListView.as_view(), name='user_list'),
    path('post/<int:id>/update/', views.PostUpdate.as_view(), name='information'),
    path('post/<int:id>/delete/', views.DeletePost.as_view(), name='information'),
]

