from adrf import viewsets
from django_filters.rest_framework import DjangoFilterBackend, OrderingFilter

import nfts.models
from nfts.serializers import NFTSerializer, NFTModelSerializer, NFTBackdropSerializer, NFTBSymbolSerializer, \
    NFTCollectionSerializer
from nfts.pagination import NFTPagination


# Create your views here.

class NFTViewSet(viewsets.ModelViewSet):
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


class BaseNFTPropertyViewSet(viewsets.ModelViewSet):
    """
    Базовый класс, который наследуют все ViewSet'ы моделей-списков свойств NFT таких как модели, коллекции символы и т.д.

    Особенности:
    - Устанавливает сортировку А-Я для сущностей в таблице по полю 'name'
    - Добавляет пагинацию с использованием NFTPagination (по умолчанию 10 элементов на страницу, максимум 100)
    - Поддерживает параметры запроса:
      * limit - количество элементов на странице (по умолчанию: 10)
      * offset - смещение от начала списка
      * ordering - поле для сортировки (по умолчанию: 'name')

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
    * `POST /api/nfts/models/` - создание новой модели NFT
    * `GET /api/nfts/models/{name}/` - получение данных конкретной модели
    * `PUT /api/nfts/models/{name}/` - обновление модели
    * `DELETE /api/nfts/models/{name}/` - удаление модели

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
    * `POST /api/nfts/backdrops/` - создание нового бекдропа
    * `GET /api/nfts/backdrops/{name}/` - получение данных конкретного бекдропа
    * `PUT /api/nfts/backdrops/{name}/` - обновление бекдропа
    * `DELETE /api/nfts/backdrops/{name}/` - удаление бекдропа

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
    * `POST /api/nfts/symbols/` - создание нового символа
    * `GET /api/nfts/symbols/{name}/` - получение данных конкретного символа
    * `PUT /api/nfts/symbols/{name}/` - обновление символа
    * `DELETE /api/nfts/symbols/{name}/` - удаление символа

    Наследуется от BaseNFTPropertyViewSet и предоставляет все его функции:
    - Сортировку по полю 'name'
    - Пагинацию (10 элементов на страницу по умолчанию)

    Работает с моделью NFTBSymbol, которая представляет символы, используемые в NFT.

    Основное поле модели:
    - name: Текстовое поле (первичный ключ)
    """
    queryset = nfts.models.NFTBSymbol.objects.all()
    serializer_class = NFTBSymbolSerializer


class NFTCollectionViewSet(BaseNFTPropertyViewSet):
    """
    ViewSet для работы с коллекциями NFT.

    Эндпоинты:
    * `GET /api/nfts/collections/` - получение списка всех коллекций
    * `POST /api/nfts/collections/` - создание новой коллекции
    * `GET /api/nfts/collections/{name}/` - получение данных конкретной коллекции
    * `PUT /api/nfts/collections/{name}/` - обновление коллекции
    * `PATCH /api/nfts/collections/{name}/` - частичное обновление коллекции
    * `DELETE /api/nfts/collections/{name}/` - удаление коллекции

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
