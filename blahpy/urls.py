from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^blog/$', 'blog.views.index'),
	url(r'^blog/archive/(?P<post_id>\d+)/$', 'blog.views.archive'),
	url(r'^blog/profile/(?P<users_id>\d+)/$', 'blog.views.profile'),
	url(r'^html/(?P<file_name>\w+)/$', 'blog.views.pageviews'),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
