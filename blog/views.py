from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Post, Comment
from .forms import CommentForm


class BlogListView(ListView):
    """
    A view that returns a list of all the blog
    posts in the database
    """
    model = Post
    template_name = 'blog.html'
    context_object_name = 'Posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        title = "Blog"
        context["title"] = title
        return context


class BlogDetailView(DetailView):
    """
    A view that returns a single blog 
    """
    model = Post
    template_name = 'blog-detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        title = "Blog"
        context["title"] = title
        return context


def add_comment_to_post(request, pk):
    """
    A view that adds a new comment to a blog post
    """
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('blog-post', pk=post.id)
    else:
        form = CommentForm()
    return render(request, 'add_comment_to_post.html', {'form': form})
