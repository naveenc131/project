from django.shortcuts import render
from django.contrib.auth import(
	authenticate,
	get_user_model,
	login,
	logout,
	)
from .forms import UserLoginForm,UserRegisterForm

# Create your views here.

def index(request):
	return render(request, 'index.html', {})

def login_view(request):
	print(request.user.is_authenticated())
	form = UserLoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		user = authenticate(username=username, password=password)
		login(request,user)
		print(request.user.is_authenticated())
	return render(request,"forms.html",{"form":form})

def register_view(request):
	form = UserRegisterForm(request.POST or None)
	if form.is_valid():
		user = form.save(commit=False)
		password = form.cleaned_data.get('password')
		user.set_password(password)
		user.save()

	return render(request,"register.html",{"form":form})

def logout_view(request):
	return render(request,"form.html",{})

