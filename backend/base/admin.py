from operator import truediv
from django.contrib import admin
from django.contrib.auth.models import Group
from .models import DocumentNumberFormat, ProjectMaster


# Register your models here.

admin.site.unregister(Group)

class adminPanelPermissionMixin:

    def has_add_permission(self, request):
        if request.user.is_superuser or request.user.is_admin:
            return True
        else:
            return False

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        else:
            return False

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        else:
            return False

    def has_view_permission(self, request, obj=None):
        if request.user.is_superuser or request.user.is_admin:
            return True
        else:
            return False


class groupAdmin(adminPanelPermissionMixin, admin.ModelAdmin):
    pass


class projectMasterAdmin(adminPanelPermissionMixin, admin.ModelAdmin) :
    pass

class documentNumberFormatAdmin(adminPanelPermissionMixin, admin.ModelAdmin):
    pass

#   list_display = ('prjId', 'category',  'subCategory', 'numberPrefix')
#   list_filter = ('prjId', 'category',  'subCategory', 'numberPrefix')

#   search_fields = ('prjId', 'category',  'subCategory', 'numberPrefix')
#   ordering = ('prjId', 'category',  'subCategory', 'numberPrefix')


#   filter_horizontal = ()


admin.site.register(Group, groupAdmin)
admin.site.register(ProjectMaster, projectMasterAdmin)
admin.site.register(DocumentNumberFormat, documentNumberFormatAdmin)
