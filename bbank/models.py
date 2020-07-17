from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django_countries.fields import CountryField
from model_utils import Choices

# Create your models here.

b=Choices('A+', 'A-', 'B+', 'B-', 'O+', 'O-', 'AB+', 'AB-')
g= Choices('Male', 'Female', 'Other')
r = Choices(1,2,3,4,5)

class Users(models.Model):
    blood_group = models.CharField(choices=b, max_length=200)
    age = models.IntegerField()
    Gender = models.CharField(choices=g, max_length=200)
    City=models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    country = CountryField(default='country')
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    contact_no = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("bbank:u_detail", kwargs={'pk': self.pk})


class Blood_Bank(models.Model):
    name = models.CharField(max_length=200)
    city=models.CharField(max_length=200)
    state=models.CharField(max_length=200)
    country=CountryField(default='country')
    h_doc = models.CharField(max_length=200)

    contact_no = models.IntegerField()
    email_id = models.EmailField()
    description = models.CharField(max_length=400)
    A = models.IntegerField(blank=True, default=0.0)
    A_mi = models.IntegerField(blank=True,default=0.0)
    B = models.IntegerField(blank=True, default=0.0)
    B_mi = models.IntegerField(blank=True, default=0.0)
    O = models.IntegerField(blank=True, default=0.0)
    O_mi = models.IntegerField(blank=True, default=0.0)
    AB = models.IntegerField(blank=True, default=0.0)
    AB_mi = models.IntegerField(blank=True, default=0.0)

    def accept(self, x, c):
        if(c=='A+' or c=='a+'):
            self.A=self.A+x
        elif(c=='A-' or c=='a-'):
            self.A_mi=self.A_mi+x
        elif (c == 'B+' or c == 'b+'):
            self.B = self.B + x
        elif (c == 'B-' or c == 'b-'):
            self.B_mi = self.B_mi + x
        elif (c == 'O+' or c == 'o+'):
            self.O= self.O + x
        elif(c=='O-' or c=='o-'):
            self.O_mi=self.O_mi+x
        elif(c=='AB' or c=='ab'):
            self.AB=self.AB+x
        elif(c=='AB-' or c=='ab-'):
            self.AB_mi=self.AB_mi+x
        self.save()


    def donate(self, x, c):

        if(c=='A+' or c=='a+'):
            self.A=self.A-x
        elif(c=='A-' or c=='a-'):
            self.A_mi=self.A_mi-x
        elif (c == 'B+' or c == 'b+'):
            self.B = self.B - x
        elif (c == 'B-' or c == 'b-'):
            self.B_mi = self.B_mi - x
        elif (c == 'O+' or c == 'o+'):
            self.O= self.O - x
        elif(c=='O-' or c=='o-'):
            self.O_mi=self.O_mi-x
        elif(c=='AB' or c=='ab'):
            self.AB=self.AB-x
        elif(c=='AB-' or c=='ab-'):
            self.AB_mi=self.AB_mi-x
        self.save()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("bbank:b_detail", kwargs={'pk': self.pk})

    def available(self, c,x):

        if(c=='A+' or c=='a+'):
            if self.A >= x:
                return True
        elif(c=='A-' or c=='a-'):
            if(self.A_mi>=x):
                return True
        elif (c == 'B+' or c == 'b+'):
            if(self.B>=x):
                return True
        elif (c == 'B-' or c == 'b-'):
            if(self.B_mi>=x):
                return True
        elif (c == 'O+' or c == 'o+'):
            if (self.O >= x):
                return True
        elif (c == 'O-' or c == 'o-'):
            if (self.O_mi >= x):
                return True
        elif (c == 'AB' or c == 'ab'):
            if (self.AB >= x):
                return True
        elif (c == 'AB-' or c == 'ab-'):
            if (self.AB_mi >= x):
                return True
        else:
            return False







class Feedback(models.Model):
    author = models.CharField(max_length=200)
    bloodbank = models.ForeignKey('bbank.Blood_Bank', related_name='feedback', on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.IntegerField(choices=r)
    date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.text

class Receiver(models.Model):
    city=models.CharField(max_length=200)
    state=models.CharField(max_length=200)
    type_req = models.CharField(max_length=200)






