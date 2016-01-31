"""django_bookmarks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
import os.path
from django.conf.urls import include, url
from django.contrib import admin
from bookmarks.views import *
from django.views.generic import TemplateView
site_media = os.path.join(
    os.path.dirname(__file__), 'site_media'
)
print site_media
urlpatterns = [
    url(r'^$', main_page),
    url(r'^user/(\w+)/$', user_page),
    url(r'^admin/$', include(admin.site.urls)),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', logout_page),
    url(r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
        { 'document_root': site_media }),
    url(r'^register/$', register_page),
    url(r'^register/success/$', TemplateView.as_view(template_name='registration/register_success.html')),
]
