from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
import graphene
from StarWarsApi.models import Character, Planet, Producer, Film
from django.contrib.auth import get_user_model



class CharacterNode(DjangoObjectType):
    id = graphene.ID(source='pk', required=True)
    class Meta:
        model = Character
        filter_fields = ['name','height','mass','gender','homeworld','films']
        interfaces = (relay.Node,)

class FilmNode(DjangoObjectType):
    id = graphene.ID(source='pk', required=True)
    class Meta:
        model = Film
        filter_fields = {
            'name':['exact'],
            'opening_crawl':['exact'],
            'character__name':['exact', 'icontains'],
            'planets':['exact'],
            'producers':['exact'],

            #['opening_crawl','director','planets','producers']
        }
        interfaces = (relay.Node,)

class PlanetNode(DjangoObjectType):
    id = graphene.ID(source='pk', required=True)
    class Meta:
        model = Planet
        filter_fields = {
            
            'name':['exact', 'icontains', 'istartswith'],
        }
        interfaces = (relay.Node,)

class ProducerNode(DjangoObjectType):
    id = graphene.ID(source='pk', required=True)
    class Meta:
        model = Producer
        filter_fields = {
            'name':['exact', 'icontains', 'istartswith'],
        }
        interfaces = (relay.Node,)

class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()


class Query(graphene.ObjectType):

    
    all_characters = DjangoFilterConnectionField(CharacterNode)
    
    all_films = DjangoFilterConnectionField(FilmNode)

    all_planets = DjangoFilterConnectionField(PlanetNode)

    all_producers = DjangoFilterConnectionField(ProducerNode)