from rest_framework import serializers
from .models import *
from django.core.files.base import ContentFile
import base64
import uuid


#이미지 base64  
class Base64ImageField(serializers.ImageField):
    """
    A Django REST framework field for handling image-uploads through raw post data.
    It uses base64 for encoding and decoding the contents of the file.

    Heavily based on
    https://github.com/tomchristie/django-rest-framework/pull/1268

    Updated for Django REST framework 3.
    """

    def to_internal_value(self, data):
        from django.core.files.base import ContentFile
        import base64
        import six
        import uuid

        # Check if this is a base64 string
        if isinstance(data, six.string_types):
            # Check if the base64 string is in the "data:" format
            if 'data:' in data and ';base64,' in data:
                # Break out the header from the base64 content
                header, data = data.split(';base64,')

            # Try to decode the file. Return validation error if it fails.
            try:
                decoded_file = base64.b64decode(data)
            except TypeError:
                self.fail('invalid_image')

            # Generate file name:
            file_name = str(uuid.uuid4())[:12] # 12 characters are more than enough.
            # Get the file name extension:
            file_extension = self.get_file_extension(file_name, decoded_file)

            complete_file_name = "%s.%s" % (file_name, file_extension, )

            data = ContentFile(decoded_file, name=complete_file_name)

        return super(Base64ImageField, self).to_internal_value(data)

    def get_file_extension(self, file_name, decoded_file):
        import imghdr

        extension = imghdr.what(file_name, decoded_file)
        extension = "jpg" if extension == "jpeg" else extension

        return extension

class Futures_LS_serializer(serializers.HyperlinkedModelSerializer):
    
    profile_url = serializers.SerializerMethodField()
    
    class Meta:
        model = Futures_article
        fields = (
            "id",
            'profile',
            'profile_url',
            'title',
            'region',
            'sub_region',
            'item',
            'price',
        )
    def get_profile_url(self, article):
            request = self.context.get('request')
            profile_url = article.profile.url
            return request.build_absolute_uri(profile_url)
        
class Futures_Full_serializer(serializers.HyperlinkedModelSerializer):
    
    profile = serializers.ImageField(use_url=True)
    
    class Meta:
        model = Futures_article
        fields = (
            "id",
            'profile',
            'title',
            'seller_name', 
            'seller_email', 
            'item', 
            'region', 
            'g_date', 
            'sub_region', 
            'quality', 
            'area', 
            'price', 
            'description', 
        )
        
class Futures_Full_GET_serializer(serializers.HyperlinkedModelSerializer):
    
    profile_url = serializers.SerializerMethodField()
    # profile = serializers.ImageField(use_url=True)
    # photo_url = serializers.SerializerMethodField(
    class Meta:
        model = Futures_article
        fields = (
            "id",
            'profile',
            'profile_url',
            'title',
            'seller_name', 
            'seller_email', 
            'item', 
            'region', 
            'g_date', 
            'sub_region', 
            'quality', 
            'area', 
            'price', 
            'description', 
        )
    def get_profile_url(self, article):
            request = self.context.get('request')
            profile_url = article.profile.url
            return request.build_absolute_uri(profile_url)
    #         if photo and hasattr(photo, 'url'):
    #         else:
    #            return None
    # def get_photo_url(self, car):
    #         request = self.context.get('request')
    #         if photo and hasattr(photo, 'url'):
    #            photo_url = car.photo.url
    #            return request.build_absolute_uri(photo_url)
    #         else:
    #            return None
        