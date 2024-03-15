from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
# Create your models here.
class Base(models.Model):
    create_at=models.DateField(auto_now_add=True)
    update_at=models.DateField(auto_now=True)

    class Meta:
        abstract =True


Custemer,Admin,Employee=['Custemer','Admin','Employee']

class User(AbstractUser,Base):
    USER_ROLLS=(
        (Custemer,Custemer),
        (Admin,Admin),
        (Employee,Employee),
    )

    phone_number=models.CharField(max_length=13)
    bio=models.CharField(max_length=250)
    user_rolls=models.CharField(max_length=25,choices=USER_ROLLS,default=Custemer)
    email=models.CharField(max_length=100,unique=True,null=True,blank=True)
    photo=models.ImageField(upload_to='user_icon/',validators=[FileExtensionValidator(allowed_extensions=['jpg','png','jpeg'])],null=True,blank=True)
    def __str__(self):
        return self.username

