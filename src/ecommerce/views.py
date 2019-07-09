from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm


def home(request):
	context = {
		'title': 'Home page',
		'content': 'Welcome to home page!'
	}
	return render(request, 'home.html', context)


def about(request):
	context = {
		'title': 'About page',
		'content': 'Welcome to about page!'
	}
	return render(request, 'home.html', context)


def contact(request):
	context = {
		'title': 'Contact page',
		'content': 'Welcome to contact page',
		'form': ContactForm()
	}
	print(request.method) # gives method name
	print(request.POST) # gives querydict
	print(request.POST.get('full_name')) # gives dict item value
	print(request.POST.get('email'))
	print(request.POST.get('content'))
	return render(request, 'contact/view.html', context)


def home_old(request):
	html_ = """
	<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">

    <title>Hello, world!</title>
  </head>
  <body>
    <h1 class='text-center'>Hello, world!</h1>

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
  </body>
</html>
	"""
	return HttpResponse(html_)
