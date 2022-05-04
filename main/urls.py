from django.urls import path
from . import views
from .views import *
from .views import EmailAttachementView


urlpatterns = [
    path('', views.home, name="home"),
    path('products/', views.products, name='products'),
    path('customer/<str:pk_test>/', views.customer, name="customer"),
    path('create_order/', views.createOrder, name="create_order"),
    path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
    path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),
    path('post/<slug:post_slug>/',views.show_post,name="post"),
    path('index', views.index, name="index"),
    path('login/', views.login, name='login'),
    path('register/', views.registration, name ='registration'),
    path('send/', EmailAttachementView.as_view(), name='emailattachment'),


]