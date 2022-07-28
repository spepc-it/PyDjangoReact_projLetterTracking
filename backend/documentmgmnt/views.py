from django.http import HttpResponse
from rest_framework import status
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import ProjectCorrespondence
from .serializers import ProjectCorrespondenceSerializer

# Create your views here.


@api_view(['GET'])
def get_ProjectCorrespondences(request):
  queryset = ProjectCorrespondence.objects.all()
  serializer = ProjectCorrespondenceSerializer(queryset, many=True)
  return Response(serializer.data)


@api_view(['GET'])
def get_ProjectCorrespondence(request, pk):
    try:
      queryset = ProjectCorrespondence.objects.get(_id=pk)
      serializer = ProjectCorrespondenceSerializer(queryset, many=False)
      return Response(serializer.data)
    except:
        return HttpResponse(status.HTTP_404_NOT_FOUND)
