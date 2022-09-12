from os import stat
from urllib import response
from django.http import HttpResponse
from django.http.response import JsonResponse
from portfolio_api.models import TestimonialModel
from portfolio_api.serializers import TestimonialFormSerializer
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.template import loader
from django.shortcuts import render


# will work on that - test kiya likn kush issues hain
class TestimonialAPI(APIView):
    
    parser_classes = [MultiPartParser, FormParser]
    
    # def get(self, request, format=None):
    #     get_all_testimonials = TestimonialModel.objects.all()
    #     serializer = TestimonialFormSerializer(get_all_testimonials, many=True)
    #     return response(serializer.data)

    def post(self, request):
        print(request.data)
        serializer = TestimonialFormSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response(serializer.data, status=status.HTTP_200_OK)
        else:
            return response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
            print('serialize: ', serializer)
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)