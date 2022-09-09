from django.http.response import JsonResponse
from portfolio_api.models import ContactFormModel
from portfolio_api.serializers import ContactFormSerializer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def contact_form_view(request):
    if request.method == 'GET':
        testimonial = ContactFormModel.objects.all()
        serializer = ContactFormSerializer(testimonial, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data_ = JSONParser().parse(request)
        serializer = ContactFormSerializer(data=data_)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    # if x_forwarded_for:
    #     ip = x_forwarded_for.split(',')[0]
    # else:
    #     ip = request.META.get('REMOTE_ADDR')
    # print(ip)
    # ```Python
    # from rest_framework import permissions

    # class BlacklistPermission(permissions.BasePermission):
    #     """
    #     Global permission check for blacklisted IPs.
    #     """

    #     def has_permission(self, request, view):
    #         ip_addr = request.META['REMOTE_ADDR']
    #         blacklisted = Blacklist.objects.filter(ip_addr=ip_addr).exists()
    #         return not blacklisted
    # ```