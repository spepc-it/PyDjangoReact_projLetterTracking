from django.contrib import admin
from base.admin import adminPanelPermissionMixin
from documentmgmnt.models import ProjectCorrespondence


# Register your models here.


class ProjectCorrespondencesAdmin(adminPanelPermissionMixin, admin.ModelAdmin):
  pass


admin.site.register(ProjectCorrespondence, ProjectCorrespondencesAdmin)
