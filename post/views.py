from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages  
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView, DetailView
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from .serializers import PostSerializer
from .models import Post
from .forms import PostForm, CommentForm
import logging

class PostListView(TemplateView):
    template_name = 'post_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        context['post_form'] = PostForm()  # Include an instance of the post form in the context
        context['comment_form'] = CommentForm()  # Include an instance of the comment form in the context
        return context
    
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')

        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'Thank you for posting!')
            return redirect('post_list')
        else:
            context = self.get_context_data()
            context['post_form'] = post_form
            return self.render_to_response(context)


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        context['comments'] = post.comments.all()  
        context['comment_form'] = CommentForm(initial={'post': post, 'author': self.request.user})
        return context

logger = logging.getLogger(__name__)
@login_required
def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        print("POST data:", request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user  # Set the author field to the logged-in user
            comment.save()
            return HttpResponseRedirect(reverse('post_detail', args=[pk]))
        else:
            # Log form errors for debugging
            logger.error(f"Invalid comment form submitted: {comment_form.errors}")
            messages.error(request, 'Error submitting comment form')
            # Redirect back to post detail page with error message
            return HttpResponseRedirect(reverse('post_detail', args=[pk]) + '?error=true')
    else:
        # Inform user to log in to perform the action
        messages.info(request, 'You need to log in to add a comment.')
        # Redirect to the login page
        return HttpResponseRedirect(reverse('login'))

# class PostViewSet(viewsets.ModelViewSet):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
