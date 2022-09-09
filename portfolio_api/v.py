from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse
from .serializers import ContactFormSerializer, TestimonialFormSerializer

# Create your views here.
from .models import ContactFormModel, TestimonialModel
from rest_framework.generics import ListAPIView
from rest_framework import generics
from rest_framework.parsers import JSONParser

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

# Testing directore structure
import rest_framework

@api_view(['GET', 'POST'])
def testimonial_view(request):
    if request.method == 'GET':
        testimonial = TestimonialModel.objects.all()
        serializer = TestimonialFormSerializer(testimonial, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data_ = JSONParser().parse(request)
        print('json result', data_, '\n \nd')
        serializer = TestimonialFormSerializer(data=data_)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
