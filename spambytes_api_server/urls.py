"""spambytes_api_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.contrib import admin
#from drf_yasg import openapi
#from drf_yasg.views import get_schema_view
#from rest_framework import permissions


# schema_view = get_schema_view(
#    openapi.Info(
#         title="SpamBytes Django API",
#         default_version='v1',
#         description="All APIs related to Spambytes Django Backend",
#         url='https://example.net/api/v1/',
#         relative_path=True
#             ),
#         public=True,
#         #permission_classes=(permissions.IsAuthenticated,),
# )


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/users/', include('apps.user.urls')),
    path('api/v1/shield/', include('apps.shield.urls')),
]
