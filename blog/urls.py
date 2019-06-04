from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.signin, name='login'),
    url(r'^logout/$', views.signout, name='logout'),
    url(r'^profile/(?P<profile_id>[0-9]+)/$', views.profile, name='profile'),
    url(r'^profile/(?P<profile_id>[0-9]+)/follow/$', views.follow, name='follow'),
    url(r'^edit_info/$', views.edit_profile, name='edit_profile'),
    url(r'^profile/new_blog$', views.new_blog, name='new_blog'),
	url(r'^blog/(?P<blog_id>[0-9]+)/blog_posts/$', views.blog_posts, name='blog_posts'),
    url(r'^blog/(?P<blog_id>[0-9]+)/new_post/', views.new_post, name='new_post'),
	url(r'^blog/(?P<blog_id>[0-9]+)/blog_posts/(?P<post_id>[0-9]+)/post/$', views.single_post, name='single_post'),
    url(r'^blog/(?P<blog_id>[0-9]+)/blog_posts/(?P<post_id>[0-9]+)/post/like/$', views.post_like, name='post_like'),
    url(r'^profile/(?P<profile_id>[0-9]+)/galery$', views.galery, name='galery'),
    url(r'^profile/(?P<profile_id>[0-9]+)/galery/add$', views.add_to_galery, name='add-galery'),
]
