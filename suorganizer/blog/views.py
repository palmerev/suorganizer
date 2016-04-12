from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from django.views.decorators.http import require_http_methods

from .models import Post


class PostList(View):
    def get(self, request):
        post_list = Post.objects.all()
        return render(
            request, 'blog/post_list.html', {'post_list': post_list})


@require_http_methods(['GET', 'HEAD'])
def post_detail(request, year, month, slug):
    post = get_object_or_404(
        Post,
        pub_date__year=year,
        pub_date__month=month,
        slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post})
