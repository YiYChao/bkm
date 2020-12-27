from django.db import models

# Create your models here.
class Publisher(models.Model):
    '''
    出版社实体
    '''
    name = models.CharField(max_length=50, null=False)      # 出版社名字


class Author(models.Model):
    '''
    作者实体
    '''
    name = models.CharField(max_length=16, null=False)      # 作者名字


class Book(models.Model):
    '''
    图书实体
    '''
    name = models.CharField(max_length=50, null=False)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)   # CASCADE, PROTECTED, SET(v), SET_DEFAULT, SET_NULL
    authors = models.ManyToManyField(Author)                # 多对多
