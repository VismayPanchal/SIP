from django.db import models

# Create your models here.

class user(models.Model):
	user_id = models.BigAutoField(primary_key=True)
	user_name = models.CharField(max_length=50, null=True, blank=True)
	user_email = models.CharField(max_length=50, null=True, blank=True)
	password = models.CharField(max_length=50, null=True, blank=True)
	class Meta:
		db_table = 'user'



    

class category(models.Model):
	cat_id = models.BigAutoField(primary_key=True)
	cat_name = models.CharField(max_length=50, null=True, blank=True)
	class Meta:
		db_table = 'category'

class sub_category(models.Model):
	sub_cat_id= models.BigAutoField(primary_key=True)
	cat_id = models.ForeignKey(category, on_delete=models.CASCADE,null=True)
	cat_name = models.CharField(max_length=50, null=True, blank=True)
	sub_cat_name=  models.CharField(max_length=50, null=True, blank=True)
	class Meta:
		db_table = 'sub_category'

class product(models.Model):
	product_id = models.BigAutoField(primary_key=True)
	product_name = models.CharField(max_length=50, null=True, blank=True)
	cat_name = models.CharField(max_length=50, null=True, blank=True)
	cat_id = models.ForeignKey(category, on_delete=models.CASCADE,null=True)
	
	sub_cat_name = models.CharField(max_length=50, null=True, blank=True)
	description = models.CharField(max_length=100, null=True, blank=True)
	price = models.IntegerField(max_length=5, null=True, blank=True)
	image = models.CharField(max_length=50, null=True, blank=True)
	stock = models.IntegerField(null=True, blank=True)
	class Meta:
		db_table= 'product'

