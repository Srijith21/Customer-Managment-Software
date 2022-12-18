from django.db import models


class Customer(models.Model):
    customer_name = models.CharField(max_length=155)
    customer_number = models.CharField(max_length=10)
    customer_email = models.EmailField()
    customer_address = models.TextField(max_length=200)
    customer_dob = models.DateField()
    info_added_on = models.DateField(auto_now=True)

    def __str__(self):
        return self.customer_name