from django.contrib import admin
from .models import Customer,Event,Tag
# Register your models here.
admin.site.register(Customer)


class EventAdmin(admin.ModelAdmin):
    list_display =["customer_name","is_published","Event_type","event_date","Event_time_type"]
admin.site.register(Event,EventAdmin)