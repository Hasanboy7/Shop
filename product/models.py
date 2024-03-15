from django.db import models
from users.models import Base,User
from django.core.validators import FileExtensionValidator
# Create your models here.

class Catigory(Base):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name='Katigoryalar'
        verbose_name_plural='Katigorya'

class Product(Base):
    user= models.ForeignKey(User,on_delete=models.CASCADE,related_name='user')
    name=models.CharField(max_length=200)
    price=models.IntegerField(default=0)
    catigory= models.ForeignKey(Catigory,on_delete=models.CASCADE,related_name='product')
    about=models.TextField(null=True,blank=True)
    image=models.ImageField(upload_to='product_img/',validators=[FileExtensionValidator(allowed_extensions=['jpg','png','jpeg'])],null=True,blank=True)
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name='Maxsulotlar'
        verbose_name_plural='Maxsulot'