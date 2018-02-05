"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path
# from portfolio import views
# from django.conf import settings
# from django.conf.urls.static import static
#
# urlpatterns = [
#     path('',views.main_page,name = 'main'),
#     path('admin/', admin.site.urls),
#     path('create/',views.post_create, name = 'create'),
#     path('detail/',views.post_detail, name = 'details'),
#     path('update/',views.post_update, name = 'update'),
#     path('delete/',views.post_delete, name = 'delete'),
#     path('post_list/',views.post_list, name = 'post_list')
#
# ]
#
#
# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
#app_name="portoflio"
from portfolio.views import home_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_page),
    path('posts/', include("portfolio.urls", namespace='posts')),
    #url(r'^posts/$', "<appname>.views.<function_name>"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
