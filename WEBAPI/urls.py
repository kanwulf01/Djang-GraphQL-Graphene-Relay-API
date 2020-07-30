from django.contrib import admin
from django.urls import path, include
from graphene_django.views import GraphQLView
from graphene_schema import schema
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphql/', GraphQLView.as_view(graphiql=True)),
    path('api/', include('StarWarsApi.urls')),
]