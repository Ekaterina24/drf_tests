from django.contrib import admin
from .models import *

# admin.site.register(Feedback)
admin.site.register(Category)
admin.site.register(Test)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(UserTestRelation)