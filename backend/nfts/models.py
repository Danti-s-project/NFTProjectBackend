from django.db import models

# Create your models here.

class NFTCollection(models.Model):
    """
    Коллекция к которой относится NFT
    """
    name = models.TextField(max_length=50, primary_key=True)
    alias = models.TextField(max_length=50, null=True)
    issued = models.IntegerField()

class NFTOwner(models.Model):
    """
    Владельцы NFT записанные в базе данных
    """
    user_id = models.IntegerField(max_length=50, primary_key=True)
    username = models.TextField(max_length=50, unique=True)

class NFTModel(models.Model):
    """
    Название модели NFT
    """
    name = models.TextField(max_length=50, primary_key=True)

class NFTBackdrop(models.Model):
    """
    Бекдроп NFT
    """
    name = models.TextField(max_length=50, primary_key=True)

class NFTBSymbol(models.Model):
    """
    symbol у NFT
    """
    name = models.TextField(max_length=50, primary_key=True)

class NFT(models.Model):
    """
    Объект хранящий конкретную NFT
    """

    collection = models.ForeignKey(NFTCollection, on_delete=models.CASCADE)
    owner = models.ForeignKey(NFTOwner, on_delete=models.CASCADE, null=True)
    nft_model = models.ForeignKey(NFTModel, on_delete=models.CASCADE)
    backdrop = models.ForeignKey(NFTBackdrop, on_delete=models.CASCADE)
    symbol = models.ForeignKey(NFTBSymbol, on_delete=models.CASCADE)
    quantity = models.IntegerField()
