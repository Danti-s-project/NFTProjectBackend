from django.urls import path

from users.views import UserViewSet, P2PCourseViewSet, NFTSellCourseViewSet, ToncoinCourseViewSet, ScamCourseViewSet

urlpatterns = [
    path('users/<int:user_id>/', UserViewSet.as_view({
        'get': 'retrieve',
        'post': 'create',
        'patch': 'partial_update',
        'delete': 'destroy',
        'put': 'update'})),
    path('p2p_course/', P2PCourseViewSet.as_view({'get': 'list'})),
    path('toncoin_course/', ToncoinCourseViewSet.as_view({'get': 'list'})),
    path('scam_course/', ScamCourseViewSet.as_view({'get': 'list'})),
    path('nft_sell_course/', NFTSellCourseViewSet.as_view({'get': 'list'}))
]
