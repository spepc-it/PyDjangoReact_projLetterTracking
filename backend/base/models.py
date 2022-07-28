from statistics import mode
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ProjectMaster(models.Model):
  _id = models.BigIntegerField("Id", primary_key=True, null=False, blank=False)
  prjTitle = models.CharField("ProjectTitle", max_length=250, null=False, blank=False)
  prjSubTitle = models.CharField("ProjectSubTitle", max_length=250, null=False, blank=False)
  createdAt = models.DateTimeField(auto_now_add=True)

  class Meta:
    verbose_name_plural = "ProjectMasters"
    ordering = ['prjTitle']
    unique_together = ['prjTitle']

  def __str__(self):
    return self.prjTitle


class DocumentNumberFormat(models.Model):
  _id = models.AutoField(primary_key=True, editable=False)
  user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=False, blank=False)
  prjId = models.ForeignKey(ProjectMaster, on_delete=models.DO_NOTHING, null=False, blank=False)
  category = models.CharField("Category", max_length=50, null=False, blank=False, default='STANDARD')
  subCategory = models.CharField("SubCategory", max_length=50, null=False, blank=False, default='STANDARD')
  numberPrefix = models.CharField("Number Prefix",max_length=50, null=False, blank=False)
  createdAt = models.DateTimeField(auto_now_add=True)

  class Meta:
    verbose_name_plural = "DocumentNumberFormats"
    # ordering = ['prjId', 'category',  'subCategory', 'numberPrefix']
    unique_together = ['prjId', 'category', 'subCategory', 'numberPrefix']

  def __str__(self):
    return self.numberPrefix

