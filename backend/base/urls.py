from django.urls import path
from . import views

urlpatterns = [
  path('projects/', views.get_Projects.as_view(), name="projects"),
  path('project/<str:pk>/', views.get_project, name='project-by-id'),
  path("documentNumberFormat/", views.get_DocumentNumberFormats.as_view(), name='documentNumberFormatFilter'),
  path('documentNumberFormat/<str:pk>/',  views.get_DocumentNumberFormatById, name='documentNumberFormat-by-id'),
  

]
