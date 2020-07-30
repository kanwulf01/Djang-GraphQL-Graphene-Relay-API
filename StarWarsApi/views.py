from django.shortcuts import render
from graphene_django.views import GraphQLView
from django.contrib.auth.mixins import LoginRequiredMixin

    
class PrivateGraphQLView(LoginRequiredMixin,GraphQLView):
    login_url = '/admin/'
    redirect_field_name = 'admin'
    pass

