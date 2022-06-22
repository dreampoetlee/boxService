from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from . serializers import ProductSerializer
from . models import Product

# Create your views here.
@api_view(['GET', 'POST'])
def product_list(request):
  if request.method == 'GET':
    product = Product.objects.all()
    serializer = ProductSerializer(product, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

  elif request.method == 'POST':
    serializer = ProductSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
def product_detail(request, pk):
  product = get_object_or_404(Product, pk=pk)
  if request.method == 'GET':
    serializer = ProductSerializer(product)
    return Response(serializer.data, status=status.HTTP_200_OK)
  elif request.method == 'PUT':
    serializer = ProductSerializer(product, data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_200_OK)
  elif request.method == 'DELETE':
    serializer = ProductSerializer(product)
    product.delete()
    return_value = serializer.data
    return_value['id'] = pk
    return Response(return_value, status=status.HTTP_204_NO_CONTENT)
  elif request.method == 'PATCH':
    serializer = ProductSerializer(product, data=request.data, partial=True)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_202_ACCEPTED)