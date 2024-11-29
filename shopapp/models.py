from django.db import models
from django.conf import settings
from accounts.models import CustomUser 

class Condition(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    
class Day(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    
class Ken(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Category(models.Model):#追加
    title = models.CharField(
        verbose_name='カテゴリ',
        max_length=20
    )

    def __str__(self):
        return self.title

class ShopPost(models.Model):
    user = models.ForeignKey(
    CustomUser,
    verbose_name='ユーザー',
    on_delete=models.CASCADE
    )

    category = models.ForeignKey(
        Category,
        verbose_name='カテゴリ',
        on_delete=models.PROTECT
    )
    
    title = models.CharField(
        verbose_name='タイトル',
        max_length=200
    )
    condition = models.ForeignKey(
        Condition, 
        on_delete=models.CASCADE, 
        null=True, blank=True
        )  
    
    day = models.ForeignKey(
        Day, 
        on_delete=models.CASCADE, 
        null=True, blank=True
        ) 
    
    ken = models.ForeignKey(
        Ken, 
        on_delete=models.CASCADE, 
        null=True, blank=True
        )
    
    price = models.CharField(
        verbose_name='商品の値段',
        max_length=10,default=' '
    )
    comment = models.TextField(
        verbose_name='コメント'
    )

    image1=models.ImageField(
        verbose_name='イメージ1',
        upload_to='photos'
    )

    image2=models.ImageField(
        verbose_name='イメージ2',
        upload_to='photos',
        blank=True,
        null=True
    )

    posted_at = models.DateTimeField(
        verbose_name='投稿日時',
        auto_now_add=True
    )
    bookmarked_by = models.ManyToManyField(CustomUser, related_name='bookmarked_products', blank=True)
    def __str__(self):
        return self.title
