from rest_framework.viewsets import ModelViewSet

from users.models import User, ScamCourse, NFTSellCourse, ToncoinCourse, P2PCourse
from users.serializer import UserSerializer, AbstractCourceSerializer


# Create your views here.
class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'user_id'


class ScamCourseViewSet(ModelViewSet):
    queryset = ScamCourse.objects.all()
    serializer_class = AbstractCourceSerializer


class NFTSellCourseViewSet(ModelViewSet):
    queryset = NFTSellCourse.objects.all()
    serializer_class = AbstractCourceSerializer


class ToncoinCourseViewSet(ModelViewSet):
    queryset = ToncoinCourse.objects.all()
    serializer_class = AbstractCourceSerializer


class P2PCourseViewSet(ModelViewSet):
    queryset = P2PCourse.objects.all()
    serializer_class = AbstractCourceSerializer