from django.shortcuts import render, get_object_or_404
from . import models,forms
from django.http import HttpResponse
from django.views import generic
from .models import Post

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse
from django.views.generic import CreateView, ListView

class Registration(CreateView):
    form_class = UserCreationForm
    success_url = '/post/'
    template_name = 'registration.html'



class NewLoginForm(LoginView):
    form_class = AuthenticationForm
    template_name = 'login.html'

    def get_success_url(self):
        return reverse("users:user_list")

class UserListView(ListView):
    queryset = User.objects.all()
    template_name = 'user_list.html'

    def get_queryset(self):
        return User.objects.all()




# Create your views here.
def blog_all(request):
    post = models.Post.objects.all()
    return render(request, 'post_list.html', {'post':post})

class PostDetail(generic.DetailView):
    template_name = 'PostDetail.html'
    def get_object(self, **kwargs):
        post_id = self.kwargs.get('id')
        return get_object_or_404(models.Post, id=post_id)

class PostCreate(generic.CreateView):
    template_name = 'PostCreate.html'
    form_class = forms.PostForm
    queryset = models.Post.objects.all()
    success_url = '/post/'
    def form_valid(self, form):
        print(form.cleaned_data)
        return super(PostCreate, self).form_valid(form=form)

class DeletePost(generic.DeleteView):
    template_name = 'delete_post.html'
    success_url = '/post/'

    def get_object(self, **kwargs):
        home_id = self.kwargs.get('id')
        return get_object_or_404(models.Post, id=home_id)

class PostUpdate(generic.UpdateView):
    template_name = 'update_post.html'
    form_class = forms.PostForm
    success_url = '/post/'

    def get_object(self, **kwargs):
        home_id = self.kwargs.get('id')
        return get_object_or_404(models.Post, id=home_id)

    def form_valid(self, form):
        return super(PostUpdate, self).form_valid(form=form)
