from rest_framework import serializers
from .models import ContactFormModel, TestimonialModel


class ContactFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactFormModel
        fields = ['full_name', 'email', 'subject', 'message', 'date_time', 'ip_address', 'city', 'country']


class TestimonialFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestimonialModel
        fields = '__all__'
