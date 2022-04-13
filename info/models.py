from django.db import models
from django.utils import timezone # django で日付を管理するためのモジュール

# Create your models here.
class Member(models.Model):
    name =models.CharField('名前',max_length=20)
    birthday=models.DateField('誕生日')
    memo=models.TextField('一言')
    icon = models.ImageField(blank=True, null=True)
    def __str__(self):
        return self.name

class Event(models.Model):
    title = models.CharField('タイトル', max_length=50)
    date=models.DateTimeField('日付',default=timezone.now)
    photo= models.ImageField(blank=True, null=True)
    deadline=models.DateTimeField('締め切り日',default=timezone.now)
    location=models.CharField('場所',max_length=50)
    text=models.TextField('内容')
    url=models.URLField('URL')
    member = models.ManyToManyField(Member,verbose_name='担当者')
