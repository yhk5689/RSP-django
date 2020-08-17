from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Product(models.Model):
	CATEGORY = (
			('한식', '한식'), 
			('퓨전', '퓨전'),
            ('서양', '퓨전'),
            ('일본','일본'),
            ('이탈리아', '이탈리아'),
            ('동남아시아', '동남아시아'),
		) 

	name = models.CharField(max_length=200, null=True)
	price = models.FloatField(null=True)
	category = models.CharField(max_length=200, null=True, choices=CATEGORY)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name

class Customer(models.Model):
	user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name

class Order(models.Model):
	STATUS = (
			('제품준비중', '제품준비중'),
			('배송중', '배송중'),
			('배송완료', '배송완료'),
			)

	customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL)
	product = models.ForeignKey(Product, null=True, on_delete= models.SET_NULL)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS)

	def __str__(self):
		return self.product.name