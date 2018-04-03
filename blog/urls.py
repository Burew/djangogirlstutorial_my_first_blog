from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views

postUrlPatterns = [
    url(r'^new/$', views.post_new, name='post_new'), 
    url(r'^(?P<pk>\d+)/$', views.post_detail, name='post_detail'), 
    url(r'^(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'), 
    url(r'^(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
    url(r'^(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
]

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'), 
    url(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
    url(r'^post/', include(postUrlPatterns)),   #for this line, done include the $ at the end of the regex
    url(r'^accounts/login/$', auth_views.login, name='login'),
    url(r'^accounts/logout/$', auth_views.logout, name='logout', kwargs={'next_page': '/'}),
]

