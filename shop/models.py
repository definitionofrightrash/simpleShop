
import datetime

from django.db import models
from django.utils import timezone
'''
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
'''

class Product(models.Model):
    Code = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=225)
    QtyInStock = models.IntegerField(default=0)
    BuyPrice = models.IntegerField()
    Description = models.CharField(max_length=500, null=True, blank=True)
    Image = models.ImageField(upload_to='static/uploads/%Y/%m/%d/', null=True, blank=True)
    AddedDate = models.DateTimeField(default=timezone.now())
    LastEdit = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return str(self.Code) + " " + self.Name + " " + str(self.BuyPrice)

    # def __init__(self, Name, BuyPrice, QtyInStock=0, Description='', Image=None):
    #     models.Model.__init__(self)
    #     self.Name = Name
    #     self.QtyInStock = QtyInStock
    #     self.BuyPrice = BuyPrice
    #     self.Description = Description
    #     if Image:
    #         self.Image = Image
    #     self.AddedDate = timezone.now()
    #     self.LastEdit = timezone.now()
        
class Customer(models.Model):
    Name = models.CharField(max_length=225)
    Email = models.EmailField(max_length=225, unique=True)
    Password = models.CharField(max_length=225)
    Credit = models.IntegerField(default=0)

'''
class Tag(models.Model):

class Category(models.Model):

class Address(models.Model):

class Order(models.Model):

class Order_Item(models.Model):
'''