"""drf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter

from tests.views import *

router = DefaultRouter()

router.register(r'categories', CategoryViewSet, basename='categories')
router.register(r'tests', TestViewSet, basename='tests')
router.register(r'questions', QuestionViewSet)
router.register(r'answers', AnswerViewSet)
router.register(r'tests_relation_view', UserTestsRelationAllView, basename='relation')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('social_django.urls', namespace='social')),
    path('auth/', auth),
    path('tests_relation_q/', UserTestsRelationQView.as_view()),
    re_path('(?P<lang>(ru|en))/', include(router.urls)),
]

urlpatterns += router.urls

