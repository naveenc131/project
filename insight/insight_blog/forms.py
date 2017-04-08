from django import forms
from django.forms import ModelForm
<<<<<<< HEAD
=======
import re
>>>>>>> 2e5afefce48b72fed9629851cd046a391bef5076

from django.contrib.auth import(
	authenticate,
	get_user_model,
	login,
	logout,
	)

User = get_user_model()


class UserLoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)


	def clean(self,*args,**kwargs):
		username = self.cleaned_data.get("username")
		password = self.cleaned_data.get("password")
		if username and password:
			user = authenticate(username=username, password=password)
			if not user:
				raise forms.ValidationError("User not exist")
			if not user.check_password(password):
				raise forms.ValidationError("Incorrect Password")
			if not user.is_active:
				raise ValidationError("This user is not active")
		return super(UserLoginForm,self).clean(*args,**kwargs)
<<<<<<< HEAD
class UserRegisterForm(forms.ModelForm):
	email = forms.EmailField(label='Email Address')
	email2 = forms.EmailField(label='Email Address')
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = User
		fields = [
			'username',
			'email',
			'email2',
			'password',

		]
	def clean_email2(self):
		email = self.cleaned_data.get('email')
		email2 = self.cleaned_data.get('email2')
		if email != email2:
			raise forms.ValidationError("Emails Must match")
		email_qs = User.objects.filter(email=email)
		if email_qs.exists():
			raise forms.ValidationError("User Already Registered")
		return email


=======




		

			
	
>>>>>>> 2e5afefce48b72fed9629851cd046a391bef5076
		
