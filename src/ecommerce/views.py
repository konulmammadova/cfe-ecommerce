from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm, LoginForm, RegisterForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model


def home(request):
	context = {
		'title': 'Home page',
		'content': 'Welcome to home page!'
	}
	if request.user.is_authenticated():
		context['premium_content'] = "YEAAHHHH"
	return render(request, 'home.html', context)


def about(request):
	context = {
		'title': 'About page',
		'content': 'Welcome to about page!'
	}
	return render(request, 'home.html', context)


def contact(request):
	contact_form = ContactForm(request.POST or None)
	context = {
		'title': 'Contact page',
		'content': 'Welcome to contact page',
		'form': contact_form
	}
	if contact_form.is_valid():
		# gives python dict => {'fullname': 'test name', 'email': 'aaa@gmail.com', 'content': 'asda'}
		print(contact_form.cleaned_data) 

	# if request.method == "POST":
	# 	print(request.method) # gives method name
	# 	print(request.POST) # gives querydict
	# 	print(request.POST.get('full_name')) # gives dict item value
	# 	print(request.POST.get('email'))
	# 	print(request.POST.get('content'))
	return render(request, 'contact/view.html', context)


def login_page(request):
	form = LoginForm(request.POST or None)
	context = {
		'form': form
	}

	# print("User logged in")
	# print(request.user.is_authenticated())

	if form.is_valid():
		print("FORM CLEANED DATA: ", form.cleaned_data)
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password')
		user = authenticate(request, username=username, password=password)
		print("USER: ", user)
		# print(request.user.is_authenticated())

		if user is not None:

			# print(request.user.is_authenticated())

			login(request, user)
			return redirect('/')
		else:
			print('Error')

	return render(request, 'auth/login.html', context)


User = get_user_model()
def register_page(request):
	form = RegisterForm(request.POST or None)
	context = {
		'form': form
	}
	if form.is_valid():
		print(form.cleaned_data)
		username = form.cleaned_data.get('username')
		email = form.cleaned_data.get('email')
		password = form.cleaned_data.get('password')
		new_user = User.objects.create_user(username=username, email=email, password=password)
		print("NEW USER: ", new_user)
		return redirect('/')

	return render(request, 'auth/register.html', context)


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
