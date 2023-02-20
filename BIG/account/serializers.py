from rest_framework import serializers
from .models import *

class UserBaseSerializer(serializers.HyperlinkedModelSerializer):
    
    profile_url = serializers.SerializerMethodField()
    back_url = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = (
            "profile",
            'profile_url',
            "back",
            'back_url',
            "username",
            "email",
            "token",
            "intro",
            "phone",
            "address",
            "kind",
            "job",
            "kindPre",
            "region",
        )
    def get_profile_url(self, User):
        request = self.context.get('request')
        profile_url = User.profile.url
        return request.build_absolute_uri(profile_url)
    def get_back_url(self, User):
            request = self.context.get('request')
            back_url = User.back.url
            return request.build_absolute_uri(back_url)

        
class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    
    profile_url = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = (
            "profile",
            'profile_url',
            "username",
            "email",
            "phone",
            "kind",
        )
    def get_profile_url(self, User):
        request = self.context.get('request')
        profile_url = User.profile.url
        return request.build_absolute_uri(profile_url)
        
class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = (
            "buyer_name",
            "seller_name",
            "buyer_birth",
            "seller_birth",
            "buyer_email",
            "seller_email",
            "buyer_address",
            "seller_address",
            "buyer_phone",
            "seller_phone",
            "farm_address",
            "item",
            "farm_area",
            "farm_date",
            "payment_date",
            "payment",
            "advance_date",
            "advance",
            "interpay_date",
            "interpay",
            "balance_date",
            "balance",
            "goods_date",
            "special_contract",
            "buyer_confirmed",
            "seller_confirmed",
        )
# class ContractSellerPreviewSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Contract
#         fields = (
#             "id",
#             "document_date",
#             "buyer_name",
#             "item", 
#         )
class ContractPreviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = (
            "id",
            "document_date",
            "buyer_name",
            "seller_name",
            "item", 
        )
# class ContractBuyerPreviewSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Contract
#         fields = (
#             "id",
#             "document_date",
#             "seller_name",
#             "item", 
#         )