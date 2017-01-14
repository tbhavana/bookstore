from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

class SignUpForm(forms.Form):
	
	username = forms.CharField(required = True,widget = forms.TextInput(attrs={'class':'form-control','placeholder':'Enter a username'}))
	email = forms.EmailField(required = True,widget = forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter your Email'}))
	password = forms.CharField(required = True,widget = forms.PasswordInput(attrs={'class':'form-control','placeholder':'Choose a password'}))
        password_again = forms.CharField(required = True,widget = forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter the Password again'}))

class LoginForm(AuthenticationForm):
	username = forms.CharField(label='', required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your Username'}))
	password = forms.CharField(label='', required=True, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Enter Your Password'}))


class CartForm(forms.Form):
	quantity = forms.IntegerField()

	