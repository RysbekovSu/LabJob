from django.shortcuts import render, get_object_or_404
from . import models,forms
from django.http import HttpResponse
from django.views import generic
from .models import Post
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

