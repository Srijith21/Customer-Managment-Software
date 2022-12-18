from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index,name="home"),
    path('events',views.events, name="events"),
    path('customer',views.customer, name="customer"),
]
