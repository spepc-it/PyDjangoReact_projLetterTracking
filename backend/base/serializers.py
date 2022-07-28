from rest_framework import serializers
from .models import ProjectMaster, DocumentNumberFormat

class ProjectMasterSerializer(serializers.ModelSerializer):
  class Meta:
    model = ProjectMaster
    fields = "__all__"


class DocumentNumberFormatSerializer(serializers.ModelSerializer):
  class Meta:
    model = DocumentNumberFormat
    fields = "__all__"
