from django.urls import path

from users.views import UserViewSet, P2PCourseViewSet, NFTSellCourseViewSet, ToncoinCourseViewSet, ScamCourseViewSet

urlpatterns = [
    path('users/', UserViewSet.as_view()),
    path('p2p_course/', P2PCourseViewSet.as_view()),
    path('toncoin_course/', ToncoinCourseViewSet.as_view()),
    path('scam_course/', ScamCourseViewSet.as_view()),
    path('nft_sell_course/', NFTSellCourseViewSet.as_view())
]