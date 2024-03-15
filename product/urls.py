from .views import about,ProductListView,ProductDetail,DetailProduct,shop,cart_summery,cart_add,cart_delete,cart_update
from django.urls import path
app_name='product'
urlpatterns = [
    path('index/',ProductListView.as_view(),name='index'),
    path('shop/',shop,name='shop'),
    path('detail/<int:id>/',DetailProduct,name='detail'),
    path('catigory/<int:pk>/',ProductDetail.as_view(),name='catigory'),
    path('cart_summery/',cart_summery,name='cart_summery'),
    path('cart_add/',cart_add,name='cart_add'),
    path('cart_update/',cart_update,name='cart_update'),
    path('cart_delete/',cart_delete,name='cart_delete'),

    path('',about,name='about')
]