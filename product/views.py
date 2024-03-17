from typing import Any
from django.contrib.sessions.models import Session
from django.shortcuts import render,get_object_or_404
from .models import Product,Catigory
from django.views.generic import ListView,DetailView
from django.http import HttpResponse,JsonResponse
from .cat import Cart
# Create your views here.

def cart_summery(request):
    cart=Cart(request)
    product=cart.get_products()
    quantity=cart.get_quantity()
    total=cart.get_total_price()
    date={
        'products':product,
        'quantity':quantity,
        'total':total
    }
    # print(product)
    # print(quantity)
    return render(request,'product/cart_summery.html',context=date)

def cartadd(request):

    cart=Cart(request)
   
    if request.POST.get("action")=='post':
        product_id=int(request.POST.get("product_id"))
        quantity=request.POST.get('product_quantity')
        # print(quantity)
        product=get_object_or_404(Product,id=product_id)
        cart.add(product=product,quantity=quantity)
        
        return JsonResponse({"product_id":product_id})
   
    return HttpResponse("Hellow word")

def cart_update(request):
    return HttpResponse("Hellow word")

def cart_delete(request):
    cart=Cart(request)
    if request.POST.get("action")=='post':
        product_id=request.POST.get('product_id')
        print(request.POST)
        cart.product_delete(product_id)
        return JsonResponse({'salom':"salom"})

def cart_update(request):
    cart=Cart(request)
   
    if request.POST.get("action")=='post':
        product_id=int(request.POST.get("product_id"))
        quantity=request.POST.get('product_quantity')
        # print(quantity)
        product=get_object_or_404(Product,id=product_id)
        cart.product_update(product=product,quantity=quantity)

    return JsonResponse({"salom":"salom"})

def DetailProduct(request,id):
    # catigory=Catigory.objects.all()
    maxsulot=Product.objects.get(id=id)
    catigory=Catigory.objects.filter(product=maxsulot)
    
    date={
        'maxsulot':maxsulot,
        'maxsulotlar':catigory,
        
    }
    
    # print(m)
    
    return render(request,'product/detail.html',context=date)

def shop(request):
    product=Product.objects.all()
    date={
        'product':product
    }
    return render(request,'product/shoping.html',context=date)

class ProductListView(ListView):
    model=Product
    template_name='product/index.html'
    context_object_name='product'
    

class ProductDetail(DetailView):
    model=Catigory
    template_name='product/index.html'
    context_object_name='product'

    def get_context_data(self,*args,**kwargs):
        context=super(ProductDetail,self).get_context_data(*args,**kwargs)
        catigory=context['product']
        context['product']=catigory.product.all()
        return context

def about(request):
    return render(request,'product/about.html')
