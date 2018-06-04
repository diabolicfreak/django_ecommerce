from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product

class ProductListView(ListView):
    queryset = Product.objects.all()

class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    
class ProductDetailSlugView(DetailView):
    queryset = Product.objects.all()

    def get_object(self, *args, **kwargs):
        slug = self.kwargs.get('slug')
        return Product.objects.filter(slug=slug).first()

class ProductFeaturedListView(ListView):
    queryset = Product.objects.all().featured()

class ProductFeaturedDetailView(DetailView):
    queryset = Product.objects.all().featured()