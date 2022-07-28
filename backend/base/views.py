from django.http import HttpResponse
from rest_framework import status
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .models import ProjectMaster, DocumentNumberFormat
from .serializers import ProjectMasterSerializer, DocumentNumberFormatSerializer

# Create your views here.

class get_Projects(generics.ListAPIView):
  queryset = ProjectMaster.objects.all()
  serializer_class = ProjectMasterSerializer
  filter_backends = [DjangoFilterBackend]
  filterset_fields = {
      'prjTitle': ['icontains'],
      'prjSubTitle': ['icontains'],  # icontains
  }


# @api_view(['GET'])
# def get_Projects(request):
  # queryset = ProjectMaster.objects.all()
  # serializer = ProjectMasterSerializer(queryset, many=True)
  # return Response(serializer.data)


@api_view(['GET'])
def get_project(request, pk):
    try:
      queryset = ProjectMaster.objects.get(_id=pk)
      serializer = ProjectMasterSerializer(queryset, many=False)
      return Response(serializer.data)
    except:
        return HttpResponse(status.HTTP_404_NOT_FOUND)


# class DocumentNumberFormatFilter(django_filters.FilterSet):
#   # subCategory__iexact = django_filters.CharFilter(
#   #     name="subCategory", lookup_expr='iexact')
#   class Meta:
#     model = DocumentNumberFormat
#     fields = {
#         'subCategory':['exact','icontains'],
#         'prjId': ['exact']
#         }

class get_DocumentNumberFormats(generics.ListAPIView):
  queryset = DocumentNumberFormat.objects.all()
  serializer_class = DocumentNumberFormatSerializer
  filter_backends = [DjangoFilterBackend]
  # filter_class = DocumentNumberFormatFilter
  filterset_fields = {
      'prjId': ['exact'],
      'category': ['iexact'],  # icontains
      'subCategory': ['iexact'], #icontains
      'numberPrefix': ['exact'],
  }
  # http://localhost:8000/api/base/documentNumberFormat/?subCategory__iexact=inward
  # http://localhost:8000/api/base/documentNumberFormat/?subCategory__icontains=inward
  # /api/base/documentNumberFormat/?subCategory__iexact=outward&prjId=20005


@api_view(['GET'])
def get_DocumentNumberFormatById(request, pk):
    try:
      queryset = DocumentNumberFormat.objects.get(_id=pk)
      serializer = DocumentNumberFormatSerializer(queryset, many=False)
    except:
        return HttpResponse(status.HTTP_404_NOT_FOUND)

    return Response(serializer.data)
