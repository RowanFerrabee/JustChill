from django.conf.urls import patterns, include, url
from django.contrib import admin
from JustChillBack import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'JustChillDjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^test/[A-z]+',views.testFunction),

    url(r'^admin/', include(admin.site.urls)),
)
