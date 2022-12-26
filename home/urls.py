from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index,name="home"),
    path('events',views.events, name="events"),

    path('events/<int:id>/',views.eventdetails, name="eventdetails"),

    path('add_events',views.add_events, name="add_events"),
    path('customer',views.customer, name="customer"),
    path('customerlist',views.customerlist, name="customerlist"),
    path('customer/<int:id>/',views.customer, name="customerupdate"),
    path('delete/<int:id>/',views.delete, name="deleteupdate"),
    path('signup',views.signup, name="signup"),
    path('login',views.login, name="login"),
]
