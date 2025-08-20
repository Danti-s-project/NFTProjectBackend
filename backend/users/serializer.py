from users.models import User


class UserSerializer:
    class Meta:
        model = User
        fields = '__all__'


class AbstractCourceSerializer:
    class Meta:
        abstract = True
        fields = '__all__'