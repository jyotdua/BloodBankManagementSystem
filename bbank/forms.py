from django import forms
from .models import Users, Feedback, Blood_Bank,Receiver
from django.contrib.auth.models import User

class UsersForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = "__all__"

class BloodBankForm(forms.ModelForm):
    class Meta:
        model=Blood_Bank
        fields = "__all__"

class FeedBackForm(forms.ModelForm):
    class Meta:
        model=Feedback
        fields='__all__'


class ReceiverForm(forms.ModelForm):

    class Meta:
        model=Receiver
        fields = "__all__"

class Userform(forms.ModelForm):

    class Meta:

        model=User
        fields=('username', 'email', 'password','first_name','last_name')
