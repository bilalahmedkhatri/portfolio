from portfolio_api.serializers import ProjectsSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from portfolio_api.models import ProjectsModel



@api_view(['GET'])
def projects_view(request):
    if request.method == 'GET':
        testimonial = ProjectsModel.objects.all()
        serializer = ProjectsSerializer(testimonial, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

