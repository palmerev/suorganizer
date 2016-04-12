from django.conf.urls import include, url
from django.contrib import admin

from organizer import urls as organizer_urls
from blog import urls as blog_urls

urlpatterns = [
    # Examples:
    # url(r'^$', 'suorganizer.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(organizer_urls)),
    url(r'^blog', include(blog_urls)),
]
