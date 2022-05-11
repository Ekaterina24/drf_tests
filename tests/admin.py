from django.contrib import admin
from .models import *

from import_export.admin import ImportExportActionModelAdmin, ExportActionMixin


class TestAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('title', 'owner')


admin.site.register(Category)
admin.site.register(Test, TestAdmin)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(UserTestRelation)
# admin.site.register(Feedback)
