"""
Сериализаторы для сервиса nfts
"""

from rest_framework import serializers

from nfts.models import NFT, NFTBackdrop, NFTModel, NFTCollection, NFTOwner, NFTSymbol


class NFTSerializer(serializers.ModelSerializer):
    """
    NFT model сериализатор
    """
    class Meta:
        model = NFT
        fields = '__all__'


class NFTCollectionSerializer(serializers.ModelSerializer):
    """
    NFT Collection сериализатор
    """
    class Meta:
        model = NFTCollection
        fields = '__all__'


class NFTBackdropSerializer(serializers.ModelSerializer):
    """
    NFT Backdrop сериализатор
    """
    class Meta:
        model = NFTBackdrop
        fields = '__all__'


class NFTModelSerializer(serializers.ModelSerializer):
    """
    NFT Model сериализатор
    """
    class Meta:
        model = NFTModel
        fields = '__all__'


class NFTOwnerSerializer(serializers.ModelSerializer):
    """
    NFT Owner сериализатор
    """
    class Meta:
        model = NFTOwner
        fields = '__all__'


class NFTSymbolSerializer(serializers.ModelSerializer):
    """
    NFT BSymbol сериализатор
    """
    class Meta:
        model = NFTSymbol
        fields = '__all__'