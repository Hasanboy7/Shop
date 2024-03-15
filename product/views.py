from typing import Any
from django.shortcuts import render,get_object_or_404
from .models import Product,Catigory
from django.views.generic import ListView,DetailView
from django.http import HttpResponse,JsonResponse
from .cat import Cart
# Create your views here.
 
def cart_summery(request):
    return HttpResponse("Hellow word")

def cart_add(request):
    cart=Cart(request)
    print(request.POST)
    if request.POST.get("action")=='post':
        product_id=int(request.POST.get("product_id"))

        product=get_object_or_404(Product,id=product_id)

        cart.add(product=product)
        return JsonResponse({"product_id":product_id})
    return HttpResponse("Hellow word")

def cart_update(request):
    return HttpResponse("Hellow word")

def cart_delete(request):
    return HttpResponse("Hellow word")



def DetailProduct(request,id):
    # catigory=Catigory.objects.all()
    maxsulot=Product.objects.get(id=id)
    catigory=Catigory.objects.filter(product=maxsulot)
    
    date={
        'maxsulot':maxsulot,
        'maxsulotlar':catigory,
        
    }
    print(maxsulot)
    print(catigory)
    
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
