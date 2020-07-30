from django.db import models

# Create your models here.


class Character(models.Model):

    name = models.CharField(max_length=500)
    height = models.CharField(max_length=500)
    mass = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
    homeworld = models.CharField(max_length=50)

class Film(models.Model):

    opening_crawl = models.CharField(max_length=1000)
    director = models.CharField(max_length=100)
    character = models.ForeignKey(Character, related_name='films' , on_delete=models.CASCADE)

class Planet(models.Model):

  name = models.CharField(max_length=50)
  poblation = models.IntegerField()
  film = models.ForeignKey(Film, related_name='planets', on_delete=models.CASCADE)


class Producer(models.Model):
  name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  filme = models.ForeignKey(Film, related_name='producers' , on_delete=models.CASCADE)
  def __str__(self):
    return self.name 