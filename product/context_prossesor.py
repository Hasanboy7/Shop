from .models import Catigory
from.cat import Cart
def catigores(request):
    return {'catigory':Catigory.objects.all()}

def cart(request):
    return {"cart":Cart(request)}