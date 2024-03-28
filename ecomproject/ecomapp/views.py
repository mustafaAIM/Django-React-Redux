from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .products import products
# Create your views here.
from .serializers import ProductSerializer
from .models import Product
@api_view(['GET'])
def getRoutes(request):
  return Response('Hello')


@api_view(['GET'])
def getProducts(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products,many = True)
    return Response(serializer.data)