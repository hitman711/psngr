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
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from rest_framework_swagger.views import get_swagger_view
from rest_framework import documentation

from . import views
from dataset.views import DataSetList

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
    # Auth User API
    path('sign-in/', views.signIn.as_view(), name='sign_in'),
    path('sign-out/', views.signOut.as_view(), name='sign_out'),
    # API rest swagger documentation
    path('rest/swagger/doc/', documentation.include_docs_urls(
        title=REST_SWAGGER_SETTINGS['title'],
        description=REST_SWAGGER_SETTINGS['description'],
        public=REST_SWAGGER_SETTINGS['public'])
    ),
    path('data-list', views.DataList.as_view(), name="data-list"),
    path('dynamic-data-list', views.DynamicDataList.as_view(),
         name="dynamic-data-list"),
    path('store-data-list', DataSetList.as_view(), name="store-data-list"),

]


if settings.STORE_DATA_IN_DB:
    from dataset.helpers import load_data_in_db
    from .helpers import cache_csv_data
    load_data_in_db(cache_csv_data(
        settings.DB_URL,
        settings.URL_OUTPUT_TYPE)
    )
