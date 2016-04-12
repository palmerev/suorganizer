from django.conf.urls import url

from .views import post_list, post_detail

urlpatterns = [
    url(r'^(?P<year>\d{4})/'
        r'^(?P<month>\d{1,2})/'
        r'^(?P<slug>[\w\-]+)/$',
        post_detail, name="blog_post_detail"),
    url(r'^$', post_list, name="blog_post_list"),
]
