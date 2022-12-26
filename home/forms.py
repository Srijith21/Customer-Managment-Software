from django import forms
from .models import Customer,Event


class DateInput(forms.DateInput):
    input_type = 'date'

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        widgets ={
            'customer_dob': DateInput(),
        }
        labels ={
            "customer_name"  : "Customer Name",
            "customer_email" : "Email Address",
            "customer_address" : " Address",
            "customer_number" : " Mobile Number",
            "customer_dob" : "Choose The Date",
        }

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        exclude = ('tag'),
        fields = '__all__'
        widgets ={
            'event_date': DateInput(),
        }
        labels ={
            "Event_type" : "Event Type",
            "Event_time_type" : "Repetition",
             
            "customer_name" : "Name of the customer",
            "is_published" : "Publish",
            
        }