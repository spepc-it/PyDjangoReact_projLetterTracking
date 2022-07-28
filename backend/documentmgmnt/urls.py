from django.contrib import admin
from django.urls import path, include
from .views import get_ProjectCorrespondences, get_ProjectCorrespondence

urlpatterns = [
    path('api/projectcorrespondences', get_ProjectCorrespondences, name='projectcorrespondences'),
    path('api/projectcorrespondence/<str:pk>/', get_ProjectCorrespondence, name='projectcorrespondences-by-id'),
]
