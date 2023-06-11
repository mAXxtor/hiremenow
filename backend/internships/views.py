from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    template_name = 'internships/index.html'


from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from . import utils
from .forms import CommentForm, PostForm
from .models import Follow, Group, Post, User


def index(request):
    posts = Post.objects.select_related('author', 'group').all()
    context = {'page_obj': utils.paginator(request, posts)}
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.select_related('author').all()
    context = {
        'group': group,
        'page_obj': utils.paginator(request, posts)
    }
    return render(request, 'posts/group_list.html', context)


class DesignView(TemplateView):
    template_name = 'internships/index.html'


class DevView(TemplateView):
    template_name = 'internships/index.html'


class ManageView(TemplateView):
    template_name = 'internships/index.html'
