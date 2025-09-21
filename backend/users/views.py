from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from users.models import User, ScamCourse, NFTSellCourse, ToncoinCourse, P2PCourse
from users.serializer import UserSerializer, P2PCourseSerializer, ToncoinCourseSerializer, ScamCourseSerializer, NFTSellCourseSerializer


# Create your views here.
class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'user_id'


class BaseCourseViewSet(ModelViewSet):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user_id']

    def get_queryset(self):
        qs = super().get_queryset()
        user_id = self.request.query_params.get("user_id")

        if user_id is not None:
            # Проверяем существование пользователя
            get_object_or_404(User, user_id=user_id)
            qs = qs.filter(user_id=user_id)

        return qs

class ScamCourseViewSet(BaseCourseViewSet):
    queryset = ScamCourse.objects.all()
    serializer_class = ScamCourseSerializer


class NFTSellCourseViewSet(BaseCourseViewSet):
    queryset = NFTSellCourse.objects.all()
    serializer_class = NFTSellCourseSerializer


class ToncoinCourseViewSet(BaseCourseViewSet):
    queryset = ToncoinCourse.objects.all()
    serializer_class = ToncoinCourseSerializer


class P2PCourseViewSet(BaseCourseViewSet):
    queryset = P2PCourse.objects.all()
    serializer_class = P2PCourseSerializer
