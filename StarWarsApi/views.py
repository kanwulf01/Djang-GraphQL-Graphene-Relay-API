from django.shortcuts import render

# Create your views here.
from graphene_django.views import GraphQLView

class PrivateGraphQLView(GraphQLView):
    pass