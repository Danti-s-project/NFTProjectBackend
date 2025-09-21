from users.models import User, ScamCourse, NFTSellCourse, ToncoinCourse, P2PCourse
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class NFTSellCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = NFTSellCourse
        fields = ['user_id', 'lesson', 'chapter']


class P2PCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = P2PCourse
        fields = ['user_id', 'lesson', 'chapter']


class ScamCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScamCourse
        fields = ['user_id', 'lesson', 'chapter']


class ToncoinCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToncoinCourse
        fields = ['user_id', 'lesson', 'chapter']
