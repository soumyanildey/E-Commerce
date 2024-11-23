from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView
from products import models
from ml_model import intersec
# Create your views here.


class SantipurView(ListView):
    template_name='Product/santipur.html'
    model=models.Category
    context_object_name='category'
    def get_queryset(self):
        # original qs
        qs = super().get_queryset() 
        # filter by a variable captured from url, for example
        return qs.filter(Type='Santipur')
    def get_context_data(self, **kwargs):
        context = super(SantipurView, self).get_context_data(**kwargs)
        context.update({
            'items': models.Products.objects.all()
        })
        return context
    
class SantiniketanView(ListView):
    template_name='Product/santiniketan.html'
    model=models.Category
    context_object_name='category'
    def get_queryset(self):
        # original qs
        qs = super().get_queryset() 
        # filter by a variable captured from url, for example
        return qs.filter(Type='Santiniketan')
    def get_context_data(self, **kwargs):
        context = super(SantiniketanView, self).get_context_data(**kwargs)
        context.update({
            'items': models.Products.objects.all()
        })
        return context
    
class KathiView(ListView):
    template_name='Product/madurkathi.html'
    model=models.Category
    context_object_name='category'
    def get_queryset(self):
        # original qs
        qs = super().get_queryset() 
        # filter by a variable captured from url, for example
        return qs.filter(Type='Kathi')
    def get_context_data(self, **kwargs):
        context = super(KathiView, self).get_context_data(**kwargs)
        context.update({
            'items': models.Products.objects.all()
        })
        return context
    
class BaluchariView(ListView):
    template_name='Product/baluchari.html'
    model=models.Category
    context_object_name='category'
    def get_queryset(self):
        # original qs
        qs = super().get_queryset() 
        # filter by a variable captured from url, for example
        return qs.filter(Type='Baluchari')
    def get_context_data(self, **kwargs):
        context = super(BaluchariView, self).get_context_data(**kwargs)
        context.update({
            'items': models.Products.objects.all()
        })
        return context
    
class ChhouView(ListView):
    template_name='Product/chhou.html'
    model=models.Category
    context_object_name='category'
    def get_queryset(self):
        # original qs
        qs = super().get_queryset() 
        # filter by a variable captured from url, for example
        return qs.filter(Type='Chhou')
    def get_context_data(self, **kwargs):
        context = super(ChhouView, self).get_context_data(**kwargs)
        context.update({
            'items': models.Products.objects.all()
        })
        return context
    
class TeracottaView(ListView):
    template_name='Product/teracotta.html'
    model=models.Category
    context_object_name='category'
    def get_queryset(self):
        # original qs
        qs = super().get_queryset() 
        # filter by a variable captured from url, for example
        return qs.filter(Type='Teracotta')
    def get_context_data(self, **kwargs):
        context = super(TeracottaView, self).get_context_data(**kwargs)
        context.update({
            'items': models.Products.objects.all()
        })
        return context
    

class ProductDetailView(DetailView):
    model=models.Products
    template_name='Product/product_details.html'
    queryset = models.Products.objects.all()
    lookup_field = 'pk'

    def get_context_data(self, **kwargs):
      context = super(ProductDetailView, self).get_context_data(**kwargs)
      current_product = self.get_object()  # This is the product object for the current page
        
        # Get the product name of the current item
      current_product_name = current_product.product_name
      recommended_products=intersec.load_model_results(current_product_name)
      context['recommended_items'] = models.Products.objects.filter(product_name__in=recommended_products)
      return context
