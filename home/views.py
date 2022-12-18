from django.shortcuts import render
from .models import Customer
from .forms import CustomerForm


def index(request):
    instance = Customer.objects.all()
    context ={
        'instance': instance
    }
    return render(request, 'index.html',context)

def customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
    form = CustomerForm()
    context = {
        'form': form
    }
    return render(request, 'customer.html',context)
def events(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
    form = CustomerForm()
    context = {
        'form': form
    }
    return render(request, 'events.html',context)
