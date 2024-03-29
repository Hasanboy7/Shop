from django.contrib.sessions.models import Session
from django.shortcuts import render
from.models import Product
class Cart:
    def __init__(self,request):
        self.session=request.session
        
        cart=self.session.get("session_key")
        date={}
        if 'session_key' not in request.session:
            cart=self.session['session_key']={}

        self.cart=cart
        
    def add(self,product,quantity):
        product_id=str(product.id)
        if product_id in self.cart:
            l="Bu maxsulotda savatingizda bor"
            
        else:
            self.cart[product_id]=str(quantity)

        self.session.modified=True


    def __len__(self):
        return len(self.cart)
    


    def get_products(self):
            product_ids=self.cart.keys()
            products=Product.objects.filter(id__in=product_ids)
            return products
    
    def get_quantity(self):
        quantity=self.cart
        return quantity
    
    def get_total_price(self):
        product_ids=self.cart.keys()
        products=Product.objects.filter(id__in=product_ids)

        total=0
        for key,value in self.cart.items():
            key=int(key)
            for product in products:
                if product.id==key:
                    total=total+(product.price*int(value))
            return total
        
    def product_delete(self,product_id):
        product_id=str(product_id)

        if product_id in self.cart:
            del self.cart[product_id]
        
        self.session.modified=True

    def product_update(self,product,quantity):
        product_id=str(product.id)
        quantity=int(quantity)

        self.cart[product_id]=quantity
        self.session.modified=True
        cart=self.cart
        return cart
        
        

class Person:
    def __init__(self,name,email):
        self.name=name
        self.email=email
        