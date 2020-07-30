from django.urls import path, include
from . import views


urlpatterns = [
    path('graphql/', views.PrivateGraphQLView.as_view(graphiql=True)),
]
