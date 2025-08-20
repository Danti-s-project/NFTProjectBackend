from django.db import models


class User(models.Model):
    """
    Информация о пользователе бота
    """
    user_id = models.IntegerField(primary_key=True)
    username = models.TextField(max_length=50)
    fullname = models.TextField(max_length=200)
    registration_date = models.DateTimeField(auto_now_add=True)
    language = models.TextField(max_length=5)
    ref_user = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    is_premium = models.BooleanField(default=False)
    balance = models.FloatField(default=0)


# Модели по курсам в боте


class BaseCourse(models.Model):
    """
    Состояние курса по тонкоину
    """

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    chapter = models.IntegerField()
    lesson = models.IntegerField()


    class Meta:
        abstract = True


class ToncoinCourse(BaseCourse):
    pass


class NFTSellCourse(BaseCourse):
    pass


class P2PCourse(BaseCourse):
    pass


class ScamCourse(BaseCourse):
    pass