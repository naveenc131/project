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
		#user.is_active=False
		user.save()
		#id=user.id
		#email=user.email
		#send_email(email,id)
		#return render(request,'thankyou.html')

	return render(request,"register.html",{"form":form})

def activate(request):
	id=int(request.GET.get('id'))
	user = User.objects.get(id=id)
	user.is_active=True
	user.save()
	return render(request,'activation.html')


def logout_view(request):
	logout(request)
	return render(request,"form.html",{})

#def send_email(toaddr,id):
#	text = "Hi!\nHow are you?\nHere is the link to activate your account:\nhttp://127.0.0.1:8000/activation/?id=%s" %(id)
	# Record the MIME types of both parts - text/plain and text/html.
#	part1 = MIMEText(text, 'plain')
#	msg = MIMEMultipart('alternative')
#	msg.attach(part1)
#	subject="Activate your account at Family Host"
#	msg="""\From: %s\nTo: %s\nSubject: %s\n\n%s""" %(fromaddr,toaddr,subject,msg.as_string())
	#Use gmail's smtp server to send email. However, you need to turn on the setting "lesssecureapps" following this link:
	#https://www.google.com/settings/security/lesssecureapps
#	server = smtplib.SMTP('smtp.gmail.com:587')
#	server.ehlo()
#	server.starttls()
#	server.login(username,password)
#	server.sendmail(fromaddr,[toaddr],msg)
#	server.quit()

