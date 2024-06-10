from django.db import models


class SignUpForm(models.Model):
	username = models.CharField(max_length=100)
	email = models.EmailField(max_length=100)
	password1 = models.CharField(max_length=50)
	password2 = models.CharField(max_length=50)




class Record(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	s_name = models.CharField(max_length=50)
	date_of_birth = models.DateField(max_length=30, blank=True)
	sex = models.CharField(max_length=15, blank=True)
	nationality = models.CharField(max_length=30, blank=True)
	state = models.CharField(max_length=20, blank=True)
	l_g_a = models.CharField(max_length=50)
	tribe = models.CharField(max_length=50)
	city = models.CharField(max_length=100)
	religion = models.CharField(max_length=50)
	blood_group = models.CharField(max_length=10)
	guidance_name = models.CharField(max_length=50)
	guidance_occupation = models.CharField(max_length=50)
	guidance_address = models.CharField(max_length=100)
	guidance_phone = models.CharField(max_length=15)
	clas = models.CharField(max_length=50)
	email = models.CharField(max_length=100, blank=True)
	admission_number = models.CharField(max_length=500)

	def __str__(self):
		return(f"{self.s_name}")

    





   

	