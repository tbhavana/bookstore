from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
	title = models.CharField(max_length = 50)
	category = models.IntegerField(default=0,editable=True)
	image = models.ImageField(upload_to='books')
	description = models.TextField()
	price = models.DecimalField(default=0,editable = True,decimal_places=2,max_digits=7) 
	author = models.CharField(max_length = 20)
	publisher = models.CharField(max_length = 20)
	age_group = models.IntegerField(default=0,editable = True) 
	genre = models.IntegerField(default = 0,editable = True)
	stock = models.IntegerField(default=0,editable = True) 
	rating = models.IntegerField(default=0,editable = True) 
	def __str__(self):
		return self.title
	
	
class Customer(models.Model):
	customer = models.OneToOneField(User)
	address = models.TextField()
	phone = models.IntegerField()
	pincode = models.IntegerField()
	def __str__(self):
		return self.customer



class Cart(models.Model):
	book = models.ForeignKey(Book)
	customer = models.ForeignKey(User)
	status = models.IntegerField(default=1,editable = True) 
	quantity = models.IntegerField(default=0,editable = True)
	






