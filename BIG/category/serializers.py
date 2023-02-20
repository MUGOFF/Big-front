from rest_framework import serializers
from .models import *

class CarrotBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrot
        fields = (
            "date",
            "value",
        )

class SeoulBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seoul
        fields = (
            "ds",
            "ythat",
            "item",
        )
class SeoulFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seoul
        fields = (
            "ds",
            "ythat",
            "yhat_lower",
            "yhat_upper",
            "item",
        )
class PusanBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pusan
        fields = (
            "ds",
            "ythat",
            "item",
        )
class PusanFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pusan
        fields = (
            "ds",
            "ythat",
            "yhat_lower",
            "yhat_upper",
            "item",
        )
        
class DaeguBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Daegu
        fields = (
            "ds",
            "ythat",
            "item",
        )
class DaeguFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = Daegu
        fields = (
            "ds",
            "ythat",
            "yhat_lower",
            "yhat_upper",
            "item",
        )
        
class GwanjuBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gwanju
        fields = (
            "ds",
            "ythat",
            "item",
        )
class GwanjuFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gwanju
        fields = (
            "ds",
            "ythat",
            "yhat_lower",
            "yhat_upper",
            "item",
        )
        
class DaejunBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Daejun
        fields = (
            "ds",
            "ythat",
            "item",
        )
class DaejunFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = Daejun
        fields = (
            "ds",
            "ythat",
            "yhat_lower",
            "yhat_upper",
            "item",
        )

###API
#seoul
class SeoulAPIBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeoulAPI
        fields = (
            "ds",
            "price",
            "ythat",
            "item",
        )
class SeoulAPIFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeoulAPI
        fields = (
            "ds",
            "price",
            "ythat",
            "yhat_lower",
            "yhat_upper",
            "item",
        )
#daegu
class DaeguAPIBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = DaeguAPI
        fields = (
            "ds",
            "price",
            "ythat",
            "item",
        )
class DaeguAPIFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = DaeguAPI
        fields = (
            "ds",
            "price",
            "ythat",
            "yhat_lower",
            "yhat_upper",
            "item",
        )
#daegjun
class DaejunAPIBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = DaejunAPI
        fields = (
            "ds",
            "price",
            "ythat",
            "item",
        )
class DaejunAPIFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = DaejunAPI
        fields = (
            "ds",
            "price",
            "ythat",
            "yhat_lower",
            "yhat_upper",
            "item",
        )
#gwanju
class GwanjuAPIBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = GwanjuAPI
        fields = (
            "ds",
            "price",
            "ythat",
            "item",
        )
class GwanjuAPIFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = GwanjuAPI
        fields = (
            "ds",
            "price",
            "ythat",
            "yhat_lower",
            "yhat_upper",
            "item",
        )
#pusan
class PusanAPIBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = PusanAPI
        fields = (
            "ds",
            "price",
            "ythat",
            "item",
        )
class PusanAPIFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = PusanAPI
        fields = (
            "ds",
            "price",
            "ythat",
            "yhat_lower",
            "yhat_upper",
            "item",
        )