from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from integ.views import user_gist_view, user_profile_view, photo_thumbnail_view, photo_full_view


urlpatterns = patterns('',
	url(r'^api/users/$', user_gist_view.UserGistList.as_view()),
	url(r'^api/users/(?P<id>[0-9a-z]+)/$', user_gist_view.UserGistDetail.as_view()),
	url(r'^api/profiles/$', user_profile_view.UserProfileList.as_view()),
	url(r'^api/profiles/(?P<id>[0-9a-z]+)/$', user_profile_view.UserProfileDetail.as_view()),
	url(r'^api/photoThumbnails/$', photo_thumbnail_view.PhotoThumbnailList.as_view()),
	url(r'^api/photoThumbnails/(?P<id>[0-9a-z]+)/$', photo_thumbnail_view.PhotoThumbnailDetail.as_view()),
	url(r'^api/photos/$', photo_full_view.PhotoFullList.as_view()),
	url(r'^api/photos/(?P<id>[0-9a-z]+)/$', photo_full_view.PhotoFullDetail.as_view()),

	#url(r'^api/posts/$', views.PostList.as_view()),
	#url(r'^api/posts/(?P<id>[0-9a-z]+)/$', views.PostDetail.as_view()),
)
urlpatterns = format_suffix_patterns(urlpatterns)