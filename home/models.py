from django.db import models

class Customer(models.Model):

    customer_name = models.CharField(max_length=155,null=True)
    customer_number = models.CharField(max_length=10)
    customer_email = models.EmailField()
    customer_address = models.TextField(max_length=200)
    customer_dob = models.DateField()
    info_added_on = models.DateField(auto_now=True)

    def __str__(self):
        return self.customer_name


class Tag(models.Model):
    tag_name= models.CharField(max_length=155)

    def __str__(self):
        return self.tag_name

class Event(models.Model):
    EVENT_CHOICES = (
    ("Birthday", "Birthday"),
    ("Marriage", "Marriage"),
    ("Anniversary", "Anniversary"),
    ("Other", "Other"),
    )
    EVENT_TIME = (
    ("Single Time Event", "Single Time Event"),
    ("Recurring Event", "Recurring Event"),
    )
    Event_type= models.CharField(max_length=155, choices =EVENT_CHOICES, default = '1')
    Event_time_type= models.CharField(max_length=155, choices =EVENT_TIME, )
    customer_name = models.ForeignKey(Customer,on_delete=models.CASCADE)
    event_date = models.DateTimeField()
    info_added_on = models.DateTimeField(auto_now=True)
    is_published=models.BooleanField(default=True)
    def __str__(self):
        return str(self.event_date)