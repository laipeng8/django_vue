from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """自定义模型"""
    mobile = models.CharField(max_length=11,unique=True,verbose_name="手机号")

    class Meta:
        db_table="dv_users"
        verbose_name ="用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username