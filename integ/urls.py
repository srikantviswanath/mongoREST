from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from integ import views


urlpatterns = patterns('',
	url(r'^api/users/$', views.UserList.as_view()),
	url(r'^api/users/(?P<id>[0-9a-z]+)/$', views.UserDetail.as_view()),
	url(r'^api/posts/$', views.PostList.as_view()),
	url(r'^api/posts/(?P<id>[0-9a-z]+)/$', views.PostDetail.as_view()),
)
urlpatterns = format_suffix_patterns(urlpatterns)