from django.conf.urls import url
from django.contrib import admin
from django.urls import path,re_path

from .views import (
	post_list,
	post_create,
	post_detail,
	post_update,
	post_delete,
	)
app_name="myproject"

urlpatterns = [
	re_path(r'^blog/$', post_list, name='list'),
    re_path(r'^create/$', post_create),
    re_path(r'^(?P<slug>[\w-]+)/$', post_detail, name='detail'),
    re_path(r'^(?P<slug>[\w-]+)/edit/$', post_update, name='update'),
    re_path(r'^(?P<slug>[\w-]+)/delete/$', post_delete),
    #url(r'^posts/$', "<appname>.views.<function_name>"),
]
