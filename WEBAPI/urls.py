from django.contrib import admin
from django.urls import path, include
from graphene_django.views import GraphQLView
from graphene_schema import schema
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('StarWarsApi.urls')),
]