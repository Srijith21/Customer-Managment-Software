from django.shortcuts import render,redirect,get_object_or_404
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login
from django.http.response import HttpResponse

from .models import Customer,Event
from .forms import CustomerForm,EventForm

from datetime import datetime,timedelta

def index(request):
    instance = Customer.objects.all()
    event_instance = Event.objects.all()
    customers_count = instance.count()
    events_count = event_instance.count()
    context ={
        'instance': instance,
        'customers_count':customers_count,
        'event_instance':event_instance,
        'events_count':events_count,
    }
    return render(request, 'index.html',context)

def customerlist(request):
    instance = Customer.objects.all()
    customers_count = instance.count()
    context ={
        'instance': instance,
        'customers_count': customers_count,
    }
    return render(request, 'customers_list.html',context)

def customer(request,id=0):
    if request.method == 'POST':
        if id==0:
            form = CustomerForm(request.POST)
        else:
            customer = Customer.objects.get(pk=id)
            form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
        return redirect('customerlist')

    else: 
        if id == 0: 
            form = CustomerForm()
        else:
            customer = Customer.objects.get(pk=id)
            form = CustomerForm(instance=customer)
        context = {
            'form': form
        }
    return render(request, 'customer.html',context)


def delete(request,id):
    customer = Customer.objects.get(pk=id)
    customer.delete()

    return redirect('customerlist')




def eventdetails(request,id):
    instance = get_object_or_404(Event.objects.filter(id=id))
    event_instance = Event.objects.filter(id=id)
    context = {
        "instance" : instance,
        'event_instance' : event_instance,
    }
    return render(request,"detail_events.html",context=context)


def events(request,id=0):

    event_instance = Event.objects.filter(is_published=True)
    all_events = Event.objects.all()

    today = datetime.today() - timedelta(days=1)
    this_day = Event.objects.filter(event_date__gte=today)

    one_week_ago = datetime.today() - timedelta(days=7)
    week = Event.objects.filter(event_date__gte=one_week_ago)

    month = datetime.today() - timedelta(days=30)
    this_month = Event.objects.filter(event_date__gte=month)

    


    sort = request.GET.get("sort")
    if sort:
        if sort == "week":
            event_instance = week
        elif sort == "today":
            event_instance = this_day
        elif sort == "month":
            event_instance = this_month
        elif sort == "all":
            event_instance = all_events

# ......................................................

    events_count = event_instance.count()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()

    form = CustomerForm()
    context = {
        'form': form,
        'event_instance':event_instance,
        'events_count' :events_count,
    }
    return render(request, 'events.html',context)



def add_events(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('events')
    form =EventForm()
    context= {
        'form': form,
    }
    return render(request, 'add_events.html',context)


def signup(request):
    if request.method == "POST":
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']

        myuser = User.objects.create_user(username,email,password)
        myuser.save()

        return redirect('login')
    
    return render(request,'signup.html')

def login(request):

    if request.method == "POST":
        username=request.POST['username']
        password = request.POST['password']

        user =authenticate(username=username, password=password)


        if user is not None:
            auth_login(request,user)
            return redirect('home')

        else:
                return redirect('signup')

    return render(request,'login.html')
    