from rest_framework import serializers
from .models import ProjectCorrespondence


class ProjectCorrespondenceSerializer(serializers.ModelSerializer):
  class Meta:
    model = ProjectCorrespondence
    fields = "__all__"

