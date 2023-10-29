from rest_framework import serializers
from .models import ContactFormModel, TestimonialModel


class ContactFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactFormModel
        fields = ['full_name', 'email', 'subject', 'message',
                  'date_time', 'ip_address', 'city', 'country']


class TestimonialFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestimonialModel
        fields = ['full_name', 'designation', 'company', 'website', 'message', 'social_media',
                  'freelance_profile', 'recommendation', 'created_date', 'status', 'test_image_02']
