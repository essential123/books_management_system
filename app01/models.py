from django.db import models


# Create your models here.

class Book(models.Model):
    """图书表"""
    title = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    publish_time = models.DateField(auto_now=True)

    publish = models.ForeignKey(to='Publish', on_delete=models.CASCADE)
    authors = models.ManyToManyField(to='Author')

    def __str__(self):
        return f'书籍对象:{self.title}'


class Publish(models.Model):
    """出版社表"""
    name = models.CharField(max_length=32)
    address = models.CharField(max_length=64)

    def __str__(self):
        return f'出版社对象:{self.name}'


class Author(models.Model):
    """作者表"""
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    author_detail = models.OneToOneField(to='AuthorDetail', on_delete=models.CASCADE)

    def __str__(self):
        return f'作者对象:{self.name}'


class AuthorDetail(models.Model):
    """作者详情表"""
    phone = models.BigIntegerField()
    address = models.CharField(max_length=64)

    def __str__(self):
        return f'作者详情对象:{str(self.phone)}|{self.address}'
