from dataclasses import fields
from rest_framework import serializers
from . models import Product

class ProductSerializer(serializers.ModelSerializer):
  class Meta:
    model = Product
    fields = ['id', 'slug', 'sku', 'name', 'description', 'image', 'stock', 'item_price']