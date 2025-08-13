from adrf import viewsets
from django_filters.rest_framework import DjangoFilterBackend, OrderingFilter

import nfts.models
from nfts.serializers import NFTSerializer, NFTModelSerializer, NFTBackdropSerializer, NFTBSymbolSerializer, \
    NFTCollectionSerializer
from nfts.pagination import NFTPagination


# Create your views here.

class NFTViewSet(viewsets.ModelViewSet):
    queryset = nfts.models.NFT.objects.all()
    serializer_class = NFTSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['collection', 'nft_model', 'backdrop', 'symbol', 'quantity']


class BaseNFTPropertyViewSet(viewsets.ModelViewSet):
    """
    Базовый класс, который наследуют все ViewSet'ы моделей-списков свойств NFT такиах как модели, коллекции символы и т.д.
    Устанавливает сортировку А-Я для сущностей в таблице, а так же добавляет пагинацию
    """

    filters_backends = [OrderingFilter]
    pagination_class = NFTPagination
    ordering_fields = ['name']
    ordering = ['name']


class NFTModelViewSet(BaseNFTPropertyViewSet):
    queryset = nfts.models.NFTModel.objects.all()
    serializer_class = NFTModelSerializer


class NFTBackdropViewSet(BaseNFTPropertyViewSet):
    queryset = nfts.models.NFTBackdrop.objects.all()
    serializer_class = NFTBackdropSerializer


class NFTSymbolViewSet(BaseNFTPropertyViewSet):
    queryset = nfts.models.NFTBSymbol.objects.all()
    serializer_class = NFTBSymbolSerializer


class NFTCollectionViewSet(BaseNFTPropertyViewSet):
    queryset = nfts.models.NFTCollection.objects.all()
    serializer_class = NFTCollectionSerializer
