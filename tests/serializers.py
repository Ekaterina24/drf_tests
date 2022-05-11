from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class TestSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Test
        fields = '__all__'

    # def test_val(self, value):
    #     if (len(value.title) > 20):
    #         raise serializers.ValidationError('Many')
    #     return value


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'


class UserTestRelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTestRelation
        fields = ('test', 'like', 'in_bookmarks', 'rate')


