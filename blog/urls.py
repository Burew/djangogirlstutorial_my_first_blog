from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'), #only empty strings will match
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'), 
]