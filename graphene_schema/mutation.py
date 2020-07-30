from django.contrib.auth import get_user_model
import graphene
from graphene_django import DjangoObjectType
from .types import CharacterNode, FilmNode, PlanetNode, ProducerNode, UserType
from StarWarsApi.models import Character, Film, Producer, Planet
import graphql_jwt


class CreateCharacterMutation(graphene.Mutation):
    class Input(object):
        name = graphene.String()
        height = graphene.String()
        mass = graphene.String()
        gender = graphene.String()
        homeworld = graphene.String()
    name = graphene.Field(CharacterNode)
    @staticmethod
    def mutate(root,info,**kwargs):
        name = kwargs.get('name').strip()
        height = kwargs.get('height').strip()
        mass = kwargs.get('mass').strip()
        gender = kwargs.get('gender').strip()
        homeworld = kwargs.get('homeworld').strip()
        obj = Character.objects.create(name=name, height=height,mass=mass,gender=gender,homeworld=homeworld)
        return CreateCharacterMutation(name=obj)

class CreateFilmMutation(graphene.Mutation):
    class Input(object):
        opening_crawl = graphene.String()
        director = graphene.String()
        character_id = graphene.Int()
    name = graphene.Field(FilmNode)
    @staticmethod
    def mutate(root,info,**kwargs):
        opening_crawl = kwargs.get('opening_crawl').strip()
        director = kwargs.get('director').strip()
        character_id = kwargs.get('character_id',0)
        obj = Film.objects.create(opening_crawl=opening_crawl,director=director,character_id=character_id)
        return CreateFilmMutation(name=obj)

class CreatePlanetMutation(graphene.Mutation):
    class Input(object):
        name = graphene.String()
        poblation = graphene.String()
        film_id = graphene.Int()
    name = graphene.Field(PlanetNode)
    @staticmethod
    def mutate(root, info, **kwargs):
        name = kwargs.get('name').strip()
        poblation = kwargs.get('poblation').strip()
        film_id = kwargs.get('film_id',0)
        obj = Planet.objects.create(name=name,poblation=poblation,film_id=film_id)
        return CreatePlanetMutation(name=obj)

class CreateProducerMutation(graphene.Mutation):
    class Input(object):
        name = graphene.String()
        last_name = graphene.String()
        filme_id = graphene.Int()
    name = graphene.Field(ProducerNode)
    @staticmethod
    def mutate(root,info, **kwargs):
        name = kwargs.get('name').strip()
        last_name = kwargs.get('last_name').strip()
        filme_id = kwargs.get('filme_id',0)
        obj = Producer.objects.create(name=name, last_name=last_name, filme_id=filme_id)
        return CreateProducerMutation(name=obj)


class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)

    def mutate(self, info, username, password, email):
        user = get_user_model()(
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save()

        return CreateUser(user=user)

class Mutation(graphene.AbstractType):
    create_character = CreateCharacterMutation.Field()
    create_film = CreateFilmMutation.Field()
    create_planet = CreatePlanetMutation.Field()
    create_producer = CreateProducerMutation.Field()
    create_user = CreateUser.Field()
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()