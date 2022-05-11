from django.db.models import Q
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, mixins
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.mixins import UpdateModelMixin, ListModelMixin, CreateModelMixin
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.response import Response

from .permissions import IsOwnerOrStaffOrReadOnly, IsAdminUserOrReadOnly, IsAdminOrReadOnly
from .serializers import *


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUserOrReadOnly, ]


class CategoryAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminOrReadOnly, )


class TestViewSetPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 10000


class TestViewSet(ModelViewSet):
    serializer_class = TestSerializer
    pagination_class = TestViewSetPagination
    filter_backends = [SearchFilter, OrderingFilter, ]
    permission_classes = [IsOwnerOrStaffOrReadOnly, ]
    search_fields = ['title']
    ordering_fields = ['title']

    def perform_create(self, serializer):
        serializer.validated_data['owner'] = self.request.user
        serializer.save()

    def get_queryset(self):
        pk = self.kwargs.get('pk')

        if not pk:
            return Test.objects.all()[:3]

        return Test.objects.filter(pk=pk)

    # добавляем маршрут для категории
    @action(methods=['get'], detail=True) # вывод категории
    def category(self, request, pk=None):
        cats = Category.objects.get(pk=pk)
        return Response({'cats': cats.title})

    @action(methods=['get'], detail=False)  # вывод категорий
    def categories(self, request):
        cats = Category.objects.all()
        return Response({'cats': [c.title for c in cats]})


# class UserTestsRelationView(UpdateModelMixin, GenericViewSet):
#     permission_classes = [IsAuthenticated, ]
#     queryset = UserTestRelation.objects.all()
#     serializer_class = UserTestRelationSerializer
#     lookup_field = 'test'
#
#     def get_object(self):
#         obj, _ = UserTestRelation.objects.get_or_create(user=self.request.user,
#                                                         test_id=self.kwargs['test'])
#         return obj


class UserTestsRelationAllView(ModelViewSet, CreateModelMixin):
    queryset = UserTestRelation.objects.all()
    serializer_class = UserTestRelationSerializer
    permission_classes = [IsAuthenticated, ]
    filter_backends = [DjangoFilterBackend, ]
    filter_fields = ['rate']


class UserTestsRelationQView(generics.ListAPIView):
    permission_classes = [IsAuthenticated, ]
    queryset = UserTestRelation.objects.filter(Q(like__startswith='1') | Q(like__startswith='2'))
    serializer_class = UserTestRelationSerializer


class TestAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    permission_classes = (IsAdminOrReadOnly, )


class QuestionViewSetPagination(PageNumberPagination):
    page_size = 6
    page_size_query_param = 'page_size'
    max_page_size = 10000


class QuestionViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    pagination_class = QuestionViewSetPagination
    permission_classes = [IsAuthenticatedOrReadOnly, ]


class AnswerViewSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10000


class AnswerViewSet(ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    pagination_class = AnswerViewSetPagination
    permission_classes = [IsAuthenticatedOrReadOnly, ]


def auth(request):
    return render(request, 'oauth.html')




