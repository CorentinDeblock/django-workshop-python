from django.shortcuts import redirect,get_object_or_404
from django.views import generic
from django.urls import reverse_lazy 
from .forms import PostForm 
from .models import Post
# Create your views here.

class index(generic.ListView):
    model = Post
    template_name="pages/index.html"
    ordering=['-created_at']

class CreatePostView(generic.CreateView): 
    model = Post
    form_class = PostForm
    template_name = 'pages/post.html'
    success_url = reverse_lazy('gallery:index')

def like(request,post_id):
    post = get_object_or_404(Post,pk=post_id)
    like = post.like + 1
    Post.objects.filter(pk=post_id).update(like=like)
    return redirect("/")

def dislike(request,post_id):
    post = get_object_or_404(Post,pk=post_id)
    dislike = post.dislike + 1
    Post.objects.filter(pk=post_id).update(dislike=dislike)
    return redirect("/")