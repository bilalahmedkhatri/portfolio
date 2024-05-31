from django.contrib import admin
from .models import ContactFormModel, TestimonialModel
# Register your models here.


@admin.register(ContactFormModel)
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'subject', 'email', 'date_time')


@admin.register(TestimonialModel)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'designation', 'company',)
