from django.contrib import admin
from .models import *
from simple_history.admin import SimpleHistoryAdmin
from simple_history import register
from django.contrib.auth.models import User
from import_export import resources, fields
from import_export.admin import ExportActionMixin

register(User)


class TestResource(resources.ModelResource):
    item_author = fields.Field(attribute='item_author', column_name='Автор')

    class Meta:
        model = Test
        fields = (
            'item_author',
            'title'
        )
        export_order = fields

    def dehydrate_item_author(self, test):
        if test.owner:
            return test.owner.username
        return ''


class TestAdmin(ExportActionMixin, admin.ModelAdmin):
    resource_class = TestResource


admin.site.register(Category)
admin.site.register(Test, TestAdmin)
admin.site.register(Question, SimpleHistoryAdmin)
admin.site.register(Answer)
admin.site.register(UserTestRelation)
# admin.site.register(Feedback)
