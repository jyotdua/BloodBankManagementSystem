from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse, Http404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Users, Blood_Bank,  Feedback
from .forms import UsersForm,BloodBankForm, FeedBackForm, ReceiverForm, Userform
from django.views.generic import (TemplateView, ListView, DetailView, DeleteView, CreateView, UpdateView)
from django.utils import timezone
from django.urls import reverse_lazy
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import generics
from django.contrib.auth.models import User
from  rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
from django.contrib.auth import get_user
from django.db.models import Q

class HomeView(TemplateView):
    template_name = 'bbank/home.html'


class BloodBankListView(ListView):
    model = Blood_Bank
    context_object_name = 'bloodbank_list'
    template_name = 'bbank/bloodbank_list.html'

    def get_queryset(self):
        return Blood_Bank.objects.all()

class UserListView(ListView):
    model=Users
    context_object_name='users_list'


class BloodBankDetailView(DetailView):
    model = Blood_Bank
    template_name = 'bbank/bloodbank_detail.html'

class UsersDetailView(DetailView):
    model=Users

def register_blood(request):
    registered = False
    form = UsersForm
    Bform = BloodBankForm
    uform = Userform
    if request.method == 'POST':
        form = UsersForm(data=request.POST)
        Bform = BloodBankForm(data=request.POST)
        uform = Userform(data=request.POST)
        if Bform.is_valid():
            bloodbank = Bform.save(commit=False)
            bloodbank.save()
        else:
            print(Bform.errors)
        if uform.is_valid():
            user = uform.save(commit=False)
            user.set_password(user.password)
            user.save()
            return redirect('login_page')

        else:
            print(form.errors)

    else:
        form = UsersForm()
        Bform = BloodBankForm()
    return render(request, 'bbank/register_blood.html',{'form': form, 'profile_form': Bform, 'userform':uform, 'registered':registered })

def register_user(request):
    registered = False
    form = UsersForm
    uform = Userform
    if request.method == 'POST':
        form=UsersForm(data=request.POST)
        uform = Userform(data=request.POST)
        if form.is_valid():
            uuser = form.save(commit=False)
            uuser.save()

            if 'profile_pic' in request.FILES:
                uuser.profile_pic = request.FILES['profile_pic']
                uuser.save()
        else:
            print(form.errors)

        if uform.is_valid():
                user = uform.save(commit=False)
                user.set_password(user.password)
                user.save()
                return redirect('login_page')

        else:
                print(uform.errors)

    else:
        form = UsersForm()
        uform = Userform()
    return render(request, 'bbank/register_user.html',{'form': form, 'userform': uform, 'registered': registered})

@login_required
def add_feedback(request, pk):
    bloodbank = get_object_or_404(Blood_Bank, pk=pk)
    if request.method == 'POST':
        form = FeedBackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.bloodbank = bloodbank
            feedback.save()
            return redirect('bbank:b_detail', pk=bloodbank.pk)
    else:
        form = FeedBackForm()
    return render(request, 'bbank/Feedback_form.html', {'form': form})




class SearchResultView(ListView):
    model = Blood_Bank
    context_object_name = 'bloodbank_list'
    template_name = 'bbank/searchresults.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Blood_Bank.objects.filter(Q(city=query)| Q(state=query))
        return object_list


class ReceiverSearchView(ListView):
    model = Blood_Bank
    context_object_name= 'bloodbank_list'
    template_name = 'bbank/receive.html'

    def get_queryset(self):
        query1 = self.request.GET.get('city')
        query2 = self.request.GET.get('blood_type')
        query3 = self.request.GET.get('quantity')

        object_list = Blood_Bank.objects.filter(Q(city = query1))
        print(list(object_list))
        obj = []
        for i in list(object_list):
            x = i.available(query2 , int(query3))
            if x is True:
                obj.append(i)
        print(obj)
        return obj



def ReceiveBlood(request):

        form = ReceiverForm
        return render(request, 'bbank/re.html', {'form': form})
@login_required
def get_blood(request, pk):
    blood_bank = get_object_or_404(Blood_Bank, pk=pk)
    type = request.GET.get('type')
    quantity = request.GET.get('Quantity')
    name=request.GET.get('name')
    email = request.GET.get('email')
    city = request.GET.get('city')
    state = request.GET.get('state')
    ZIP = request.GET.get('ZIP')

    if(blood_bank.available(type,int(quantity))):
        blood_bank.donate(int(quantity), type)
        blood_bank.save()
        return render(request,'bbank/receipt.html',{'name':name, 'email':email, 'city':city, 'state':state, 'ZIP':ZIP, 'quantity': quantity, 'type':type, 'pik':pk})
    else:
        return  HttpResponse('Sorry this Blood_Type is not available')
@login_required
def Donate(request,pk):
    blood_bank = get_object_or_404(Blood_Bank,pk=pk)
    type = request.GET.get('type')
    quantity = request.GET.get('Quantity')
    blood_bank.accept(int(quantity),type)
    blood_bank.save()
    return redirect('bbank:b_detail', pk=blood_bank.pk)



