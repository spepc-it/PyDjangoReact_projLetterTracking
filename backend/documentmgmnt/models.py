from statistics import mode
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User

from base.models import DocumentNumberFormat, ProjectMaster

# from backend.base.models import DocumentNumberFormat, ProjectMaster

# Create your models here.


class ProjectCorrespondence(models.Model):
  _id = models.AutoField(primary_key=True, editable=False)
  prjId = models.ForeignKey(ProjectMaster, on_delete=models.DO_NOTHING, null=False, blank=False)
  coresponType = models.ForeignKey(DocumentNumberFormat, on_delete=models.DO_NOTHING, null=False, blank=False)
  corensonNumner = models.BigIntegerField("Sequence Number", null=False, blank=False)
  coresponDate = models.DateField("Document Date", null=False, blank=False)
  coresponClassification = models.CharField("Classification", max_length=1000, null=False, blank=False)
  coresponSubject = models.CharField("Subject", max_length=1000, null=False, blank=False)
  briefDescription = models.CharField("Brief Description", max_length=3000, null=True, blank=True)
  hasAttachment = models.BooleanField("Has Attachment", null=False, blank=False, default=False)
  actionTakenOn = models.CharField("Action Taken On", max_length=3000, null=True, blank=True)
  isOpen = models.BooleanField("Is Open", null=False, blank=False, default=True)
  fileName = models.CharField("File Name", max_length=255, null=True, blank=True)
  filePath = models.CharField("File Path", max_length=255, null=True, blank=True)
  fileType = models.CharField("File Type", max_length=15, null=True, blank=True)
  remarks = models.CharField("Remarks", max_length=3000, null=True, blank=True)
  createdBy = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=False, blank=False, related_name="projcoresp_createdBy")
  createdOn = models.DateTimeField(auto_now_add=True)
  modifiedBy = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True, related_name="projectcoresp_modifiedBy")
  modifiedOn = models.DateTimeField("Modified On", null=True, blank=True)

  class Meta:
    verbose_name_plural = "ProjectCorrespondences"
    ordering = ['prjId', 'coresponType', 'corensonNumner']
    unique_together = ['prjId', 'coresponType', 'corensonNumner']

  def __str__(self):
    return self.coresponSubject


