from django.urls import path

from nfts.views import NFTViewSet, NFTModelViewSet, NFTBackdropViewSet, NFTSymbolViewSet, NFTCollectionViewSet
urlpatterns = [
    # NFT endpoints
    path('nfts/', NFTViewSet.as_view({'get': 'list'}), name='nft-list'),
    path('nfts/<int:pk>/', NFTViewSet.as_view({
        'get': 'retrieve',
    }), name='nft-detail'),

    # NFT Models endpoints
    path('models/', NFTModelViewSet.as_view({'get': 'list'}), name='model-list'),
    path('models/<str:pk>/', NFTModelViewSet.as_view({
        'get': 'retrieve',
    }), name='model-detail'),

    # NFT Backdrops endpoints
    path('backdrops/', NFTBackdropViewSet.as_view({'get': 'list'}), name='backdrop-list'),
    path('backdrops/<str:pk>/', NFTBackdropViewSet.as_view({
        'get': 'retrieve',
    }), name='backdrop-detail'),

    # NFT Symbols endpoints
    path('symbols/', NFTSymbolViewSet.as_view({'get': 'list'}), name='symbol-list'),
    path('symbols/<str:pk>/', NFTSymbolViewSet.as_view({
        'get': 'retrieve',
    }), name='symbol-detail'),

    # NFT Collections endpoints
    path('collections/', NFTCollectionViewSet.as_view({'get': 'list'}), name='collection-list'),
    path('collections/<str:pk>/', NFTCollectionViewSet.as_view({
        'get': 'retrieve',
    }), name='collection-detail')
]