"""psngr URL Configuration

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
from django.contrib import admin
from django.urls import path, include

from rest_framework_swagger.views import get_swagger_view
from rest_framework import documentation

from . import views

schema_view = get_swagger_view(title='psngr project API configuration')

# REST Swagger configuration
REST_SWAGGER_SETTINGS = {
    "title": "psngr project API configuration",
    "description":
    "List of all API end points for all psngr project",
    "public": False
}

urlpatterns = [
    path('admin/', admin.site.urls),
    # Backend structure doc
    path('back/doc/', include('django.contrib.admindocs.urls')),
    # API Swagger documentation
    path('swagger/doc/', schema_view),
    # API rest swagger documentation
    path('rest/swagger/doc/', documentation.include_docs_urls(
        title=REST_SWAGGER_SETTINGS['title'],
        description=REST_SWAGGER_SETTINGS['description'],
        public=REST_SWAGGER_SETTINGS['public'])
    ),
    path('data-list', views.DataList.as_view(), name="data-list")

]
