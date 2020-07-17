from django.conf.urls import url
from bbank import views
from django.urls import path
from rest_framework.routers import DefaultRouter
from django.conf.urls import include
from rest_framework.schemas import get_schema_view


app_name = 'bbank'

urlpatterns = [
    url(r'^$',views.HomeView.as_view(), name='home'),
    url(r'^blood_banks/$', views.BloodBankListView.as_view(), name='b_list'),

    url(r'^blood_banks/(?P<pk>\d+)$', views.BloodBankDetailView.as_view(), name='b_detail'),
    url(r'^users/$', views.UserListView.as_view(), name='user_list'),
    url(r'users/(?P<pk>\d+)/detail/$', views.UsersDetailView.as_view(), name='u_detail'),
    url('search/', views.SearchResultView.as_view(), name='Search_results'),
    url(r'receiver/$', views.ReceiverSearchView.as_view(), name='ReceiverSearch'),
    url(r'receiveblood/$', views.ReceiveBlood, name='ReceiveBlood'),
    url(r'^register/blood/$', views.register_blood, name='Register_blood'),
    url(r'^register/user/$', views.register_user, name='Register_user'),
    url(r'^blood_banks/(?P<pk>\d+)/feedback/$', views.add_feedback, name='add_feedback'),
    url(r'^blood_banks/(?P<pk>\d+)/get_blood',views.get_blood, name='get_blood'),
    url(r'^blood_banks/(?P<pk>\d+)/donate', views.Donate, name='Donate')
]