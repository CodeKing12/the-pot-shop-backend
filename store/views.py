from .models import Product, ProductGroup, Category
from store.api.serializers import ProductSerializer, GroupSerializer, CategorySerializer
from rest_framework import generics
from django_filters import rest_framework as filters
from rest_framework.filters import OrderingFilter
from .filters import ProductFilter
import time

# Create your views here.
class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetails(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    lookup_field = "slug"
    serializer_class = ProductSerializer

class GroupDetails(generics.RetrieveAPIView):
    time.sleep(5)
    lookup_field = "name"
    queryset = ProductGroup.objects.all()
    serializer_class = GroupSerializer

class CategoryDetails(generics.RetrieveUpdateAPIView):
    lookup_field = "slug"
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class SearchProducts(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.DjangoFilterBackend, OrderingFilter]
    filterset_class = ProductFilter
    ordering_fields = ['name', 'price', 'created_at']
    # filterset_fields = ["name", "short_description", "category", "price", "composition"]
