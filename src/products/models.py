from django.db import models
import random
import os


def get_filename_ext(filepath):
	base_name = os.path.basename(filepath)
	name, ext = os.path.splitext(base_name)
	return name, ext


def upload_image_path(instance, filename):
	print('instance: ', instance)
	print('filename: ', filename)
	new_filename = random.randint(1,324245)
	name, ext = get_filename_ext(filename)
	final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
	return "products/{new_filename}/{final_filename}".format(new_filename=new_filename, final_filename=final_filename)



class ProductManager(models.Manager):
	# you can override default method like this:
	# def all():
	# 	return something

	# Extending model manager by wtiring new method, not overriding 
	def get_by_id(self, id):
		qs = self.get_queryset().filter(id=id)
		if qs:
			return qs.first()
		else:
			return None
		# self.get_queryset == Product.objects


class Product(models.Model):
	title = models.CharField(max_length=120)
	description = models.TextField()
	price = models.DecimalField(decimal_places=2, max_digits=20, default=39.99)
	# image = models.FileField(upload_to='products/', null=True, blank=True)
	image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)

	objects = ProductManager()

	def __str__(self):
		return self.title

	# for python 2 use unicode instead str	
	def __unicode__(self):
		return self.title