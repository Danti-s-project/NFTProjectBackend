from users.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class AbstractCourceSerializer(serializers.ModelSerializer):
    class Meta:
        abstract = True
        fields = '__all__'