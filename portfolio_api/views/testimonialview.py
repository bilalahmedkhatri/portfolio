from django.http import HttpResponse
from django.http.response import JsonResponse
from portfolio_api.models import TestimonialModel
from portfolio_api.serializers import TestimonialFormSerializer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.template import loader
from django.shortcuts import render

def testimonial_form_submittion(request):
    temp = loader.get_template("testimonialform.html")
    return HttpResponse(temp.render())

@api_view(['GET', 'POST'])
def testimonial_view(request):
    if request.method == 'GET':
        testimonial = TestimonialModel.objects.all()
        serializer = TestimonialFormSerializer(testimonial, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data_ = JSONParser().parse(request)
        serializer = TestimonialFormSerializer(data=data_)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)