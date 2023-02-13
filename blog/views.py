from django.shortcuts import render, get_object_or_404
from .models import Post
from django.http import Http404, HttpResponseRedirect
from django.views.generic import ListView, DetailView
from blog.models import Post, Comment
from blog.forms import CommentForm


class PostListView(ListView):
    queryset = Post.objects.all().order_by('-date')
    context_object_name = 'Posts'
    template_name = 'blog/blog.html'
    paginate_by = 1


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post.html'


def post(request, id):
    post = get_object_or_404(Post, id=id)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST, author=request.user, post=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path)

    return render(request, "blog/post.html", {"post": post, "form": form})
