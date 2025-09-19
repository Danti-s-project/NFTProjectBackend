from django.contrib import admin

from nfts.models import NFT, NFTCollection, NFTOwner, NFTSymbol, NFTBackdrop, NFTModel

# Register your models here.


admin.site.register(NFT)
admin.site.register(NFTCollection)
admin.site.register(NFTOwner)
admin.site.register(NFTSymbol)
admin.site.register(NFTBackdrop)
admin.site.register(NFTModel)
