
from django.urls import path
from.import views

urlpatterns = [

    path('',views.index,name="index"),
    path('signup',views.signup,name="signup"),
    path('logedin',views.logedin,name="logedin"),
    path('cart_item', views.cart_item, name="cart_item"),
    path('display_cart', views.display_cart, name="display_cart"),
    path('log_out',views.log_out,name="log_out"),
    path("search",views.search,name="search"),
    path("checkout", views.checkout, name="checkout"),
    path("user", views.user, name="user"),
    path("feedback", views.feedback, name="feedback"),




]