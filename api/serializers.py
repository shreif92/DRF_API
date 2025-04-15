from rest_framework import serializers
from .models import *


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class Categoryserializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'