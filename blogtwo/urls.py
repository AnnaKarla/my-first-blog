from django.conf.urls import  url
from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),s
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$',
        views.post_new,
        name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$',
        views.post_edit, name='post_edit'),
    ]
