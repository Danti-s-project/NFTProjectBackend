from adrf import viewsets
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

import nfts.models
from nfts.serializers import NFTSerializer, NFTModelSerializer, NFTBackdropSerializer, NFTSymbolSerializer, \
    NFTCollectionSerializer
from nfts.pagination import NFTPagination


# Create your views here.

class NFTViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet для работы с объектами NFT.

    Предоставляет CRUD операции для управления NFT объектами.

    Эндпоинты:
    * `GET /api/nfts/nfts/` - получение списка всех NFT с фильтрацией
    * `POST /api/nfts/nfts/` - создание нового NFT
    * `GET /api/nfts/nfts/{id}/` - получение данных конкретного NFT
    * `PUT /api/nfts/nfts/{id}/` - полное обновление NFT
    * `PATCH /api/nfts/nfts/{id}/` - частичное обновление NFT
    * `DELETE /api/nfts/nfts/{id}/` - удаление NFT

    Поддерживает фильтрацию по полям: 
    * collection - коллекция NFT
    * nft_model - модель NFT
    * backdrop - фон NFT
    * symbol - символ NFT
    * quantity - количество

    Пример запроса с фильтрацией:
    `GET /api/nfts/nfts/?collection=AlphaNFT&symbol=BTC`
    """
    queryset = nfts.models.NFT.objects.all()
    serializer_class = NFTSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['collection', 'nft_model', 'backdrop', 'symbol', 'quantity']


class BaseNFTPropertyViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Базовый класс, который наследуют все ViewSet'ы моделей-списков свойств NFT таких как модели, коллекции символы и т.д.

    Особенности:
    - Устанавливает сортировку А-Я для сущностей в таблице по полю 'name'
    - Добавляет пагинацию с использованием NFTPagination (по умолчанию 10 элементов на страницу, максимум 100)
    - Поддерживает параметры запроса:
      * limit - количество элементов на странице (по умолчанию: 10)
      * offset - смещение от начала списка
      * ordering - поле для сортировки (по умолчанию: 'name')

    Доступные методы:
    * GET - получение списка элементов и детальной информации

    Пример запроса с пагинацией и сортировкой:
    `GET /api/nfts/collections/?limit=5&offset=10&ordering=-name`
    """

    filter_backends = [OrderingFilter]
    pagination_class = NFTPagination
    ordering_fields = ['name']
    ordering = ['name']


class NFTModelViewSet(BaseNFTPropertyViewSet):
    """
    ViewSet для работы с моделями NFT.

    Эндпоинты:
    * `GET /api/nfts/models/` - получение списка всех моделей NFT
    * `GET /api/nfts/models/{name}/` - получение данных конкретной модели

    Наследуется от BaseNFTPropertyViewSet и предоставляет все его функции:
    - Сортировку по полю 'name'
    - Пагинацию (10 элементов на страницу по умолчанию)

    Работает с моделью NFTModel, которая представляет название модели NFT.

    Основное поле модели:
    - name: Текстовое поле (первичный ключ)
    """
    queryset = nfts.models.NFTModel.objects.all()
    serializer_class = NFTModelSerializer


class NFTBackdropViewSet(BaseNFTPropertyViewSet):
    """
    ViewSet для работы с бекдропами NFT.

    Эндпоинты:
    * `GET /api/nfts/backdrops/` - получение списка всех бекдропов
    * `GET /api/nfts/backdrops/{name}/` - получение данных конкретного бекдропа

    Наследуется от BaseNFTPropertyViewSet и предоставляет все его функции:
    - Сортировку по полю 'name'
    - Пагинацию (10 элементов на страницу по умолчанию)

    Работает с моделью NFTBackdrop, которая представляет бекдроп (фон) NFT.

    Основное поле модели:
    - name: Текстовое поле (первичный ключ)
    """
    queryset = nfts.models.NFTBackdrop.objects.all()
    serializer_class = NFTBackdropSerializer


class NFTSymbolViewSet(BaseNFTPropertyViewSet):
    """
    ViewSet для работы с символами NFT.

    Эндпоинты:
    * `GET /api/nfts/symbols/` - получение списка всех символов
    * `GET /api/nfts/symbols/{name}/` - получение данных конкретного символа

    Наследуется от BaseNFTPropertyViewSet и предоставляет все его функции:
    - Сортировку по полю 'name'
    - Пагинацию (10 элементов на страницу по умолчанию)

    Работает с моделью NFTSymbol, которая представляет символы, используемые в NFT.

    Основное поле модели:
    - name: Текстовое поле (первичный ключ)
    """
    queryset = nfts.models.NFTSymbol.objects.all()
    serializer_class = NFTSymbolSerializer


class NFTCollectionViewSet(BaseNFTPropertyViewSet):
    """
    ViewSet для работы с коллекциями NFT.

    Эндпоинты:
    * `GET /api/nfts/collections/` - получение списка всех коллекций
    * `GET /api/nfts/collections/{name}/` - получение данных конкретной коллекции

    Наследуется от BaseNFTPropertyViewSet и предоставляет все его функции:
    - Сортировку по полю 'name'
    - Пагинацию (10 элементов на страницу по умолчанию)

    Работает с моделью NFTCollection, которая представляет коллекции NFT.

    Поля модели:
    - name: Текстовое поле (первичный ключ)
    - alias: Альтернативное название (может быть null)
    - indexed: Целочисленное поле для индексации (по умолчанию 0)
    - quantity: Количество элементов в коллекции
    """
    queryset = nfts.models.NFTCollection.objects.all()
    serializer_class = NFTCollectionSerializer
