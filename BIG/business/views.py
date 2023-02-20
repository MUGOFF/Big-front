from django.shortcuts import render
from .models import *
import base64
from .serializers import *
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser


# Create your views here.
class Article_List(APIView):
    parser_classes = (MultiPartParser, FormParser, )
    def get(self,request,formatter=None):
        region=request.GET.get('region')
        sub_region=request.GET.get('sub_region')
        item=request.GET.get('item')
        price=request.GET.get('price',0)
        print(region=='')
        if region!='' and sub_region!='' and item!='':
            articles=Futures_article.objects.filter(region=region, sub_region=sub_region, item=item, price__gte=price)
        elif region!='' and sub_region=='' and item!='':
            articles=Futures_article.objects.filter(region=region,item=item,price__gte=price)
        elif region!='' and sub_region=='' and item=='':
            articles=Futures_article.objects.filter(region=region,price__gte=price)
        elif region!='' and sub_region!='' and item=='':
            articles=Futures_article.objects.filter(region=region, sub_region=sub_region, price__gte=price)
        elif region=='' and item!='':
            articles=Futures_article.objects.filter(item=item, price__gte=price)
        else:
            articles=Futures_article.objects.filter(price__gte=price)
        serializer = Futures_LS_serializer(articles, many=True, context={"request": request})
        return Response(serializer.data)
    def post(self,request,formatter=None):
        print(request.data)
        # img_string = request.data['img_base64'] # POST요청을 통해 받은 base64정보
        # imgdata = base64.b64decode(img_string) # 디코딩
        # image = request.data['data']['profile']
        # print(type(image))
        Futures_article = Futures_Full_serializer(data=request.data) #Request의 data를 UserSerializer로 변환
        print(Futures_article)
        if Futures_article.is_valid():
            Futures_article.save() #UserSerializer의 유효성 검사를 한 뒤 DB에 저장
            return Response(Futures_article.data, status=status.HTTP_201_CREATED) #client에게 JSON response 전달
        else:
            return Response(Futures_article.errors, status=status.HTTP_400_BAD_REQUEST)
        
class Article_Info(APIView):
    parser_classes = (MultiPartParser, FormParser, )
    def get(self,request,formatter=None):
        id = request.GET.get('id')
        article = Futures_article.objects.filter(id=id)
        serializer = Futures_Full_GET_serializer(article, many=True, context={"request": request})
        return Response(serializer.data)
        