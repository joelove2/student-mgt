from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record



class SignUpForm(UserCreationForm):
	email = forms.EmailField(label="Email Addresss", widget=forms.TextInput(attrs={'class':'form-control'}))
	first_name = forms.CharField(label="First Name", max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
	last_name = forms.CharField(label="Last Name", max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))


	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

	username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Your username',
        'class':'w-full py-2 px-3 rounded-xl'
    }))
	first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Your first name',
        'class':'w-full py-2 px-3 rounded-xl'
    }))
	last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Your last name',
        'class':'w-full py-2 px-3 rounded-xl'
    }))
	email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder':'Your email',
        'class':'w-full py-2 px-3 rounded-xl'
    }))
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Your password',
        'class':'w-full py-2 px-3 rounded-xl'
    }))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Confirm password',
        'class':'w-full py-2 px-3 rounded-xl'
    }))
    
    


	

# Create Add Record Form
class AddRecordForm(forms.ModelForm):
	s_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={ "class":"form-control"}), label="Student Name")
	date_of_birth = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={ "class":"form-control"}), label="Date of Birth")
	sex = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={ "class":"form-control"}), label="Sex")
	nationality = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={ "class":"form-control"}), label="Nationality")
	state = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={ "class":"form-control"}), label="State")
	l_g_a = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={ "class":"form-control"}), label="L.G.A")
	tribe = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={ "class":"form-control"}), label="Tribe")
	city = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={ "class":"form-control"}), label="City")
	religion = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={ "class":"form-control"}), label="Religion")
	blood_group = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={ "class":"form-control"}), label="Blood Group")
	guidance_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={ "class":"form-control"}), label="Guidance's Name")
	guidance_occupation = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={ "class":"form-control"}), label="Guidance's Occupation")
	guidance_address = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={ "class":"form-control"}), label="Guidance's Address")
	guidance_phone = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={ "class":"form-control"}), label=" Guidance's Phone Number")
	clas = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={ "class":"form-control"}), label="Class")
	email = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={ "class":"form-control"}), label="Email Address")
	admission_number = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={ "class":"form-control"}), label="Admission Number")
	

	class Meta:
		model = Record
		exclude = ("user",)

class AForm(forms.Form):
    s_name = forms.CharField(max_length=30, label="Student Name")
   




	

