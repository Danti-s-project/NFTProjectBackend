from django.urls import path

from nfts.views import NFTViewSet, NFTModelViewSet, NFTBackdropViewSet, NFTSymbolViewSet, NFTCollectionViewSet
urlpatterns = [
    path('nfts/', NFTViewSet.as_view({'get': 'list'}), name='nft-list'),
    path('models/', NFTModelViewSet.as_view({'get': 'list'}), name='model-list'),
    path('backdrops/', NFTBackdropViewSet.as_view({'get': 'list'}), name='backdrop-list'),
    path('symbols/', NFTSymbolViewSet.as_view({'get': 'list'}), name='symbol-list'),
    path('collections/', NFTCollectionViewSet.as_view({'get': 'list'}), name='collection-list')
]