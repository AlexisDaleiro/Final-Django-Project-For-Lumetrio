from django.http import HttpResponse
from django.shortcuts import render, redirect
from profiles.views import Profile, ProfileDetailView, ProfileListView, ProfileModelForm
from posts.views import PostDeleteView, PostUpdateView, post_comment_create_and_list_view
from posts.models import Post
from posts.forms import PostModelForm, CommentModelForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required




def home_view(request):
    qs = Post.objects.all()
    c_form = CommentModelForm()
    p_form = PostModelForm()

    context = {
        'qs': qs,
        'p_form': p_form,
        'c_form': c_form,
    }

    return render(request, 'main/home.html', context)
    # return HttpResponse('Hello World')

# class ViewAnonym(UserPassesTestMixin, LoginRequiredMixin):
    # model = Post
    # template_name = 'main/home.html'
    # success_url = reverse_lazy('posts:main-post-view')
