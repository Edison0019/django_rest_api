from rest_framework import serializers
from . import models
import base64
from django.conf import settings
import os

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Restaurant
        fields = ['id','name','direction','phone']

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ingredient
        fields = ['id', 'name']

class RecipeSerializer(serializers.ModelSerializer):
    thumbnail = serializers.SerializerMethodField('encode_thumbnail')
    ingredients = serializers.SerializerMethodField('get_ingredients')

    def encode_thumbnail(self,recipe):
        with open(os.path.join(settings.MEDIA_ROOT,recipe.thumbnail.name),'rb') as image_file:
            return base64.b64encode(image_file.read)
    
    