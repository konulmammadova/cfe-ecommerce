from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Product
from django.views.generic import ListView, DetailView
# Create your views here.


class ProductFeaturedListview(ListView):
	template_name = 'products/list.html'

	def get_queryset(self, *args, **kwargs):
		# return Product.objects.features()
		return Product.objects.all().featured()


class ProductFeaturedDetailview(DetailView):
	template_name = 'products/featured-detail.html'

	def get_queryset(self):
		pk = self.kwargs.get('pk')
		# qs = Product.objects.features()
		qs = Product.objects.filter(pk=pk).featured()
		return qs


class ProductListview(ListView):
	# queryset = Product.objects.all()
	template_name = 'products/list.html'

	# Every cbv has this method => get_context_data
	# def get_context_data(self, *args, **kwargs):
	# 	context = super(ProductListview, self).get_context_data(*args, **kwargs)
	# 	print(context)
	# 	return context

	# intead of queryset (on the top in class) can be used get_queryset method
	def get_queryset(self, *args, **kwargs):
		return Product.objects.all()


def product_list_view(request):
	queryset = Product.objects.all()
	context = {
		'object_list': queryset
	}
	return render(request, 'products/list.html', context)


class ProductDetailSlugview(DetailView):
	queryset = Product.objects.all()
	template_name = 'products/detail.html'

	def get_object(self, *args, **kwargs):
		request = self.request
		slug = self.kwargs.get('slug')
		# instance = get_object_or_404(Product, slug=slug, active=True)
		try:
			instance = Product.objects.get(slug=slug)
		except Product.DoesNotExist:
			raise Http404("Not found...")
		except Product.MultipleObjectsReturned:
			qs = Product.objects.filter(slug=slug)
			instance = qs.first()
		except:
			raise Http404('Uhmmm')
		return instance


class ProductDetailview(DetailView):
	# queryset = Product.objects.all()
	template_name = 'products/detail.html'

	# Every cbv has this method => get_context_data
	# def get_context_data(self, *args, **kwargs):
	# 	context = super(ProductListview, self).get_context_data(*args, **kwargs)
	# 	print(context)
	# 	return context

	# Using custom model manager method in cbv detailview
	# def get_object(self, *args, **kwargs):
	# 	request = self.request
	# 	pk = self.kwargs.get('pk')
	# 	instance = Product.objects.get_by_id(pk)
	# 	if instance is None:
	# 		raise Http404("No product found in cbv detailview")
	# 	return instance
	# Since we use get_object we do not need queryset on the top(commented)

	# Instead of queryset or get_object can be used get_queryset
	def get_queryset(self, *args, **kwargs):
		pk = self.kwargs.get('pk')
		qs = Product.objects.filter(pk=pk)
		print('I AM HERE')
		return qs

def product_detail_view(request, pk, *args, **kwargs):
	# print(args)
	# print(kwargs)
	# queryset = Product.objects.get(pk=pk)

	# 1
	# Instead of get  can be used get_or_404
	# queryset = get_object_or_404(Product, pk=pk)
	# ############################################

	# 2
	# For detailed explanation alternative get_or_404
	# try:
	# 	queryset = Product.objects.get(pk=pk)
	# except Product.DoesNotExist:
	# 	print("no product")
	# 	raise Http404("No product here")
	# except:
	# 	print('huh?')
	# ###############################################

	# 3
	# queryset = Product.objects.filter(pk=pk)
	# if queryset.count() == 1:
	# 	queryset = queryset.first()
	# else:
	# 	raise Http404("No product here 2")

	# NOTE: objects is representitive form of model manager. 
	#       objects is model manager.
	# 		filter, get are model maganer's methods
	# ###############################################

	# 4
	queryset = Product.objects.get_by_id(pk)
	if queryset is None:
		raise Http404("Product did not found")
	# ###############################################

	context = {
		'object': queryset
	}
	return render(request, 'products/detail.html', context)



