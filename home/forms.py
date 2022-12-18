from django import forms
from .models import Customer


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
            'customer_name ' : "Customer Name",
            'customer_email ' : "Email Address",
            'customer_address ' : " Address",
            'customer_number ' : " Phone Number",
            'customer_dob ' : "Choose The Date",
        }
