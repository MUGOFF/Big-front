from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
import csv
import datetime
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
import requests, json
import pandas as pd
import numpy as np
import datetime as DT
import joblib
from prophet import Prophet 
from aimodel.models import *




# Create your views here.
class CarrotRealPrice(APIView):
    def get(self,request, formatter=None):
        prices = Carrot.objects.all()
        serializer = CarrotBaseSerializer(prices, many=True)
        return Response(serializer.data)
    
class SeoulItemPrice(APIView):
    def get(self,request,formatter=None):
        item = request.GET.get('item', 'pepper')
        expand = request.GET.get('expand', False)
        prices = Seoul.objects.filter(item=item)
        if expand:
            serializer = SeoulFullSerializer(prices, many=True)
        else:
            serializer = SeoulBaseSerializer(prices, many=True)
        return Response(serializer.data)
    
class PusanItemPrice(APIView):
    def get(self,request,formatter=None):
        item = request.GET.get('item', 'carrot')
        expand = request.GET.get('expand', False)
        prices = Pusan.objects.filter(item=item)
        if expand:
            serializer = PusanFullSerializer(prices, many=True)
        else:
            serializer = PusanBaseSerializer(prices, many=True)
        return Response(serializer.data)
    
class DaeguItemPrice(APIView):
    def get(self,request,formatter=None):
        item = request.GET.get('item', 'carrot')
        expand = request.GET.get('expand', False)
        prices = Daegu.objects.filter(item=item)
        if expand:
            serializer = DaeguFullSerializer(prices, many=True)
        else:
            serializer = DaeguBaseSerializer(prices, many=True)
        return Response(serializer.data)
    
class GwanjuItemPrice(APIView):
    def get(self,request,formatter=None):
        item = request.GET.get('item', 'carrot')
        expand = request.GET.get('expand', False)
        prices = Gwanju.objects.filter(item=item)
        if expand:
            serializer = GwanjuFullSerializer(prices, many=True)
        else:
            serializer = GwanjuBaseSerializer(prices, many=True)
        return Response(serializer.data)
    
class DaejunItemPrice(APIView):
    def get(self,request,formatter=None):
        item = request.GET.get('item', 'carrot')
        expand = request.GET.get('expand', False)
        prices = Daejun.objects.filter(item=item)
        if expand:
            serializer = DaejunFullSerializer(prices, many=True)
        else:
            serializer = DaejunBaseSerializer(prices, many=True)
        return Response(serializer.data)
##API 
#seoul   
class SeoulItemAPIPrice(APIView):
    def get(self,request,formatter=None):
        #테이블 초기화
        init_table =  SeoulAPI.objects.all()[:]
        for row in init_table:
            row.delete()
        #url 파라미터
        item = request.GET.get('item', 'carrot')
        past = int(request.GET.get('past', 30))
        period = int(request.GET.get('period', 30))
        expand = request.GET.get('expand', True)
        #실 가격 데이터
        if past !=0:
            today = DT.date.today()
            startday = today - DT.timedelta(days=past)
            codelist=[
                ['200','232',['01']], #당근
                ['200','231',['06']], #무 '01','02','03','06'
                ['400','412',['01']], #배
                ['200','211',['03']], #배추 '01','02','03','06'
                ['200','214',['01']], #상추
                ['200','221',['00']], #수박
                ['200','213',['00']], #시금치
                ['200','212',['00']], #양배추
                ['200','223',['03']], #오이
                ['200','225',['00']], #토마토
                ['200','242',['00']], #풋고추
            ]
            item_list = [
                'carrot',
                'radish',
                'pear',
                'napacabbage',
                'lettuce',
                'watermelon',
                'spinach',
                'cabbage',
                'cucumber',
                'tomato',
                'pepper',
            ]
            item_index = item_list.index(item)
            url = f"http://www.kamis.or.kr/service/price/xml.do?action=periodProductList&p_startday={str(startday)}&p_endday={str(today)}&p_itemcategorycode={codelist[item_index][0]}&p_itemcode={codelist[item_index][1]}&p_kindcode={codelist[item_index][2][0]}&p_productrankcode=04&p_countrycode=1101&p_convert_kg_yn=N&p_cert_key=55809923-b691-4da7-89ea-68e0b445bb26&p_cert_id=3038&p_returntype=json"
            response = requests.post(url)
            data = response.json()
            # print(data)
            date_list = []
            for i in range(past):
                date = startday+DT.timedelta(days=i)
                date_list.append(date)
            test_df = pd.DataFrame(date_list, columns=['ds'])
            test_df['item'] = item
            test_df['price'] = np.nan
            for price_data in data['data']['item']:
                if price_data['countyname']=='서울':
                    api_date = DT.datetime.strptime(price_data['yyyy']+'/'+price_data['regday'], "%Y/%m/%d").date()
                    test_df.loc[test_df['ds']==api_date,'price'] = int(price_data['price'].replace(",",''))
            test_df = test_df.interpolate(method='linear')
            test_df = test_df.fillna(method='bfill')
            test_df = test_df.fillna(method='ffill')
            for index, row in test_df.iterrows():
                seoul_api = SeoulAPI()
                seoul_api.item = row['item']
                seoul_api.price = row['price']
                seoul_api.ds = row['ds']
                seoul_api.save()
            # print(test_df)
        #가격 예측 데이터
        if period !=0 :
            model = Aimodel.objects.filter(select =True, item= item, region='seoul')[0]
            model_path = model.file.path
            # print(model_path)
            loaded_model = joblib.load(model_path)
            # print('loaded')
            # print('beforemake', DT.datetime.now())
            future = loaded_model.make_future_dataframe(periods=500)
            future['cap'] = model.cap
            future['floor'] = model.floor
            future1 =future.loc[future['ds']>=DT.datetime.today()-DT.timedelta(days=1)].reset_index(drop=True)
            # print('make', DT.datetime.now())
            forecast = loaded_model.predict(future1)
            # print('predict', DT.datetime.now())
            for n in range(period):
                category = SeoulAPI()
                category.ds = forecast['ds'][n] 
                category.ythat = forecast['yhat'][n] 
                category.yhat_lower = forecast['yhat_lower'][n] 
                category.yhat_upper = forecast['yhat_upper'][n]
                category.item = item
                category.save()
            # print('save', DT.datetime.now())
        prices = SeoulAPI.objects.filter(item=item)
        if expand:
            serializer = SeoulAPIFullSerializer(prices, many=True)
        else:
            serializer = SeoulAPIBaseSerializer(prices, many=True)
        return Response(serializer.data)
#daegu    
class DaeguItemAPIPrice(APIView):
    def get(self,request,formatter=None):
        #테이블 초기화
        init_table =  DaeguAPI.objects.all()[:]
        for row in init_table:
            row.delete()
        #url 파라미터
        item = request.GET.get('item', 'carrot')
        past = int(request.GET.get('past', 30))
        period = int(request.GET.get('period', 30))
        expand = request.GET.get('expand', True)
        #실 가격 데이터
        if past !=0:
            today = DT.date.today()
            startday = today - DT.timedelta(days=past)
            codelist=[
                ['200','232',['01']], #당근
                ['200','231',['06']], #무 '01','02','03','06'
                ['400','412',['01']], #배
                ['200','211',['03']], #배추 '01','02','03','06'
                ['200','214',['01']], #상추
                ['200','221',['00']], #수박
                ['200','213',['00']], #시금치
                ['200','212',['00']], #양배추
                ['200','223',['03']], #오이
                ['200','225',['00']], #토마토
                ['200','242',['00']], #풋고추
            ]
            item_list = [
                'carrot',
                'radish',
                'pear',
                'napacabbage',
                'lettuce',
                'watermelon',
                'spinach',
                'cabbage',
                'cucumber',
                'tomato',
                'pepper',
            ]
            item_index = item_list.index(item)
            url = f"http://www.kamis.or.kr/service/price/xml.do?action=periodProductList&p_startday={str(startday)}&p_endday={str(today)}&p_itemcategorycode={codelist[item_index][0]}&p_itemcode={codelist[item_index][1]}&p_kindcode={codelist[item_index][2][0]}&p_productrankcode=04&p_countrycode=2200&p_convert_kg_yn=N&p_cert_key=55809923-b691-4da7-89ea-68e0b445bb26&p_cert_id=3038&p_returntype=json"
            response = requests.post(url)
            data = response.json()
            date_list = []
            for i in range(past):
                date = startday+DT.timedelta(days=i)
                date_list.append(date)
            test_df = pd.DataFrame(date_list, columns=['ds'])
            test_df['item'] = item
            test_df['price'] = np.nan
            for price_data in data['data']['item']:
                if price_data['countyname']=='대구':
                    api_date = DT.datetime.strptime(price_data['yyyy']+'/'+price_data['regday'], "%Y/%m/%d").date()
                    test_df.loc[test_df['ds']==api_date,'price'] = int(price_data['price'].replace(",",''))
            test_df = test_df.interpolate(method='linear')
            test_df = test_df.fillna(method='bfill')
            for index, row in test_df.iterrows():
                daegu_api = DaeguAPI()
                daegu_api.item = row['item']
                daegu_api.price = row['price']
                daegu_api.ds = row['ds']
                daegu_api.save()
        #가격 예측 데이터
        if period !=0 :
            model = Aimodel.objects.filter(select =True, item= item, region='daegu')[0]
            model_path = model.file.path
            loaded_model = joblib.load(model_path)
            future = loaded_model.make_future_dataframe(periods=500)
            future['cap'] = model.cap
            future['floor'] = model.floor
            future1 =future.loc[future['ds']>=DT.datetime.today()-DT.timedelta(days=1)].reset_index(drop=True)
            forecast = loaded_model.predict(future1)
            for n in range(period):
                category = DaeguAPI()
                category.ds = forecast['ds'][n] 
                category.ythat = forecast['yhat'][n] 
                category.yhat_lower = forecast['yhat_lower'][n] 
                category.yhat_upper = forecast['yhat_upper'][n]
                category.item = item
                category.save()
            
        prices = DaeguAPI.objects.filter(item=item)
        if expand:
            serializer = DaeguAPIFullSerializer(prices, many=True)
        else:
            serializer = DaeguAPIBaseSerializer(prices, many=True)
        return Response(serializer.data)
#pusan    
class PusanItemAPIPrice(APIView):
    def get(self,request,formatter=None):
        #테이블 초기화
        init_table =  PusanAPI.objects.all()[:]
        for row in init_table:
            row.delete()
        #url 파라미터
        item = request.GET.get('item', 'carrot')
        past = int(request.GET.get('past', 30))
        period = int(request.GET.get('period', 30))
        expand = request.GET.get('expand', True)
        #실 가격 데이터
        if past !=0:
            today = DT.date.today()
            startday = today - DT.timedelta(days=past)
            codelist=[
                ['200','232',['01']], #당근
                ['200','231',['06']], #무 '01','02','03','06'
                ['400','412',['01']], #배
                ['200','211',['03']], #배추 '01','02','03','06'
                ['200','214',['01']], #상추
                ['200','221',['00']], #수박
                ['200','213',['00']], #시금치
                ['200','212',['00']], #양배추
                ['200','223',['03']], #오이
                ['200','225',['00']], #토마토
                ['200','242',['00']], #풋고추
            ]
            item_list = [
                'carrot',
                'radish',
                'pear',
                'napacabbage',
                'lettuce',
                'watermelon',
                'spinach',
                'cabbage',
                'cucumber',
                'tomato',
                'pepper',
            ]
            item_index = item_list.index(item)
            url = f"http://www.kamis.or.kr/service/price/xml.do?action=periodProductList&p_startday={str(startday)}&p_endday={str(today)}&p_itemcategorycode={codelist[item_index][0]}&p_itemcode={codelist[item_index][1]}&p_kindcode={codelist[item_index][2][0]}&p_productrankcode=04&p_countrycode=2100&p_convert_kg_yn=N&p_cert_key=55809923-b691-4da7-89ea-68e0b445bb26&p_cert_id=3038&p_returntype=json"
            response = requests.post(url)
            data = response.json()
            date_list = []
            for i in range(past):
                date = startday+DT.timedelta(days=i)
                date_list.append(date)
            test_df = pd.DataFrame(date_list, columns=['ds'])
            test_df['item'] = item
            test_df['price'] = np.nan
            for price_data in data['data']['item']:
                if price_data['countyname']=='부산':
                    api_date = DT.datetime.strptime(price_data['yyyy']+'/'+price_data['regday'], "%Y/%m/%d").date()
                    test_df.loc[test_df['ds']==api_date,'price'] = int(price_data['price'].replace(",",''))
            test_df = test_df.interpolate(method='linear')
            test_df = test_df.fillna(method='bfill')
            for index, row in test_df.iterrows():
                pusan_api = PusanAPI()
                pusan_api.item = row['item']
                pusan_api.price = row['price']
                pusan_api.ds = row['ds']
                pusan_api.save()
        #가격 예측 데이터
        if period !=0 :
            model = Aimodel.objects.filter(select =True, item= item, region='pusan')[0]
            model_path = model.file.path
            loaded_model = joblib.load(model_path)
            future = loaded_model.make_future_dataframe(periods=500)
            future['cap'] = model.cap
            future['floor'] = model.floor
            future1 =future.loc[future['ds']>=DT.datetime.today()-DT.timedelta(days=1)].reset_index(drop=True)
            forecast = loaded_model.predict(future1)
            for n in range(period):
                category = PusanAPI()
                category.ds = forecast['ds'][n] 
                category.ythat = forecast['yhat'][n] 
                category.yhat_lower = forecast['yhat_lower'][n] 
                category.yhat_upper = forecast['yhat_upper'][n]
                category.item = item
                category.save()
            
        prices = PusanAPI.objects.filter(item=item)
        if expand:
            serializer = PusanAPIFullSerializer(prices, many=True)
        else:
            serializer = PusanAPIBaseSerializer(prices, many=True)
        return Response(serializer.data)
#daejun    
class DaejunItemAPIPrice(APIView):
    def get(self,request,formatter=None):
        #테이블 초기화
        init_table =  DaejunAPI.objects.all()[:]
        for row in init_table:
            row.delete()
        #url 파라미터
        item = request.GET.get('item', 'carrot')
        past = int(request.GET.get('past', 30))
        period = int(request.GET.get('period', 30))
        expand = request.GET.get('expand', True)
        #실 가격 데이터
        if past !=0:
            today = DT.date.today()
            startday = today - DT.timedelta(days=past)
            codelist=[
                ['200','232',['01']], #당근
                ['200','231',['06']], #무 '01','02','03','06'
                ['400','412',['01']], #배
                ['200','211',['03']], #배추 '01','02','03','06'
                ['200','214',['01']], #상추
                ['200','221',['00']], #수박
                ['200','213',['00']], #시금치
                ['200','212',['00']], #양배추
                ['200','223',['03']], #오이
                ['200','225',['00']], #토마토
                ['200','242',['00']], #풋고추
            ]
            item_list = [
                'carrot',
                'radish',
                'pear',
                'napacabbage',
                'lettuce',
                'watermelon',
                'spinach',
                'cabbage',
                'cucumber',
                'tomato',
                'pepper',
            ]
            item_index = item_list.index(item)
            url = f"http://www.kamis.or.kr/service/price/xml.do?action=periodProductList&p_startday={str(startday)}&p_endday={str(today)}&p_itemcategorycode={codelist[item_index][0]}&p_itemcode={codelist[item_index][1]}&p_kindcode={codelist[item_index][2][0]}&p_productrankcode=04&p_countrycode=2501&p_convert_kg_yn=N&p_cert_key=55809923-b691-4da7-89ea-68e0b445bb26&p_cert_id=3038&p_returntype=json"
            response = requests.post(url)
            data = response.json()
            date_list = []
            for i in range(past):
                date = startday+DT.timedelta(days=i)
                date_list.append(date)
            test_df = pd.DataFrame(date_list, columns=['ds'])
            test_df['item'] = item
            test_df['price'] = np.nan
            for price_data in data['data']['item']:
                if price_data['countyname']=='대전':
                    api_date = DT.datetime.strptime(price_data['yyyy']+'/'+price_data['regday'], "%Y/%m/%d").date()
                    test_df.loc[test_df['ds']==api_date,'price'] = int(price_data['price'].replace(",",''))
            test_df = test_df.interpolate(method='linear')
            test_df = test_df.fillna(method='bfill')
            for index, row in test_df.iterrows():
                daejun_api = DaejunAPI()
                daejun_api.item = row['item']
                daejun_api.price = row['price']
                daejun_api.ds = row['ds']
                daejun_api.save()
        #가격 예측 데이터
        if period !=0 :
            model = Aimodel.objects.filter(select =True, item= item, region='daejun')[0]
            model_path = model.file.path
            loaded_model = joblib.load(model_path)
            future = loaded_model.make_future_dataframe(periods=500)
            future['cap'] = model.cap
            future['floor'] = model.floor
            future1 =future.loc[future['ds']>=DT.datetime.today()-DT.timedelta(days=1)].reset_index(drop=True)
            forecast = loaded_model.predict(future1)
            for n in range(period):
                category = DaejunAPI()
                category.ds = forecast['ds'][n] 
                category.ythat = forecast['yhat'][n] 
                category.yhat_lower = forecast['yhat_lower'][n] 
                category.yhat_upper = forecast['yhat_upper'][n]
                category.item = item
                category.save()
            
        prices = DaejunAPI.objects.filter(item=item)
        if expand:
            serializer = DaejunAPIFullSerializer(prices, many=True)
        else:
            serializer = DaejunAPIBaseSerializer(prices, many=True)
        return Response(serializer.data)
#gwanju    
class GwanjuItemAPIPrice(APIView):
    def get(self,request,formatter=None):
        #테이블 초기화
        init_table =  GwanjuAPI.objects.all()[:]
        for row in init_table:
            row.delete()
        #url 파라미터
        item = request.GET.get('item', 'carrot')
        past = int(request.GET.get('past', 30))
        period = int(request.GET.get('period', 30))
        expand = request.GET.get('expand', True)
        #실 가격 데이터
        if past !=0:
            today = DT.date.today()
            startday = today - DT.timedelta(days=past)
            codelist=[
                ['200','232',['01']], #당근
                ['200','231',['06']], #무 '01','02','03','06'
                ['400','412',['01']], #배
                ['200','211',['03']], #배추 '01','02','03','06'
                ['200','214',['01']], #상추
                ['200','221',['00']], #수박
                ['200','213',['00']], #시금치
                ['200','212',['00']], #양배추
                ['200','223',['03']], #오이
                ['200','225',['00']], #토마토
                ['200','242',['00']], #풋고추
            ]
            item_list = [
                'carrot',
                'radish',
                'pear',
                'napacabbage',
                'lettuce',
                'watermelon',
                'spinach',
                'cabbage',
                'cucumber',
                'tomato',
                'pepper',
            ]
            item_index = item_list.index(item)
            url = f"http://www.kamis.or.kr/service/price/xml.do?action=periodProductList&p_startday={str(startday)}&p_endday={str(today)}&p_itemcategorycode={codelist[item_index][0]}&p_itemcode={codelist[item_index][1]}&p_kindcode={codelist[item_index][2][0]}&p_productrankcode=04&p_countrycode=1101&p_convert_kg_yn=N&p_cert_key=55809923-b691-4da7-89ea-68e0b445bb26&p_cert_id=3038&p_returntype=json"
            response = requests.post(url)
            data = response.json()
            date_list = []
            for i in range(past):
                date = startday+DT.timedelta(days=i)
                date_list.append(date)
            test_df = pd.DataFrame(date_list, columns=['ds'])
            test_df['item'] = item
            test_df['price'] = np.nan
            for price_data in data['data']['item']:
                if price_data['countyname']=='광주':
                    api_date = DT.datetime.strptime(price_data['yyyy']+'/'+price_data['regday'], "%Y/%m/%d").date()
                    test_df.loc[test_df['ds']==api_date,'price'] = int(price_data['price'].replace(",",''))
            test_df = test_df.interpolate(method='linear')
            test_df = test_df.fillna(method='bfill')
            for index, row in test_df.iterrows():
                gwanju_api = GwanjuAPI()
                gwanju_api.item = row['item']
                gwanju_api.price = row['price']
                gwanju_api.ds = row['ds']
                gwanju_api.save()
        #가격 예측 데이터
        if period !=0 :
            model = Aimodel.objects.filter(select =True, item= item, region='gwanju')[0]
            model_path = model.file.path
            loaded_model = joblib.load(model_path)
            future = loaded_model.make_future_dataframe(periods=500)
            future['cap'] = model.cap
            future['floor'] = model.floor
            future1 =future.loc[future['ds']>=DT.datetime.today()-DT.timedelta(days=1)].reset_index(drop=True)
            forecast = loaded_model.predict(future1)
            for n in range(period):
                category = GwanjuAPI()
                category.ds = forecast['ds'][n] 
                category.ythat = forecast['yhat'][n] 
                category.yhat_lower = forecast['yhat_lower'][n] 
                category.yhat_upper = forecast['yhat_upper'][n]
                category.item = item
                category.save()
            
        prices = GwanjuAPI.objects.filter(item=item)
        if expand:
            serializer = GwanjuAPIFullSerializer(prices, many=True)
        else:
            serializer = GwanjuAPIBaseSerializer(prices, many=True)
        return Response(serializer.data)
   



# def  DataInsert(request):
#     path = 'D:/AIVLE/Project Web Code/BIG/static/csv/se_당근_2023.csv'
#     file = open(path)
#     reader = csv.reader(file)
#     datalist = []
#     print('----', reader)
#     for row in reader:
#         # print(row[0])
#         # print(type(row[0]))
#         # date_data = datetime.datetime.strptime(row[0])
#         # print(date_data)
#         datalist.append(Carrot(date=row[0], value=row[1], estimated_value_low=row[2], estimated_value_high=row[3]))
#     Carrot.objects.bulk_create(datalist)
#     return HttpResponse('Insert Complete')
    