from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.core.paginator import Paginator
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserBaseSerializer

class UserProfile(APIView):
    def get(self, request, formatter=None):
        email = request.GET.get('email')
        profile = User.objects.filter(email=email)
        serializer = UserProfileSerializer(profile, many=True, context={"request": request})
        return Response(serializer.data)


class UserUpdateView(APIView):
    def put(self,request,formatters=None):
        token=request.GET.get('token',None)
        user_list = User.objects.get(token=token)
        if user_list != None:
            update_user = UserBaseSerializer(user_list, data=request.data)
            if update_user.is_valid():
                update_user.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return Response(update_user.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class Contract_doc(APIView):
    def get(self,request,formatters=None):
        id = int(request.GET.get('id'))
        contract = Contract.objects.filter(id=id)
        serializer = ContractSerializer(contract, many=True)
        return Response(serializer.data)
    def put(self,request,formatters=None):
        id = int(request.GET.get('id'))
        contract = Contract.objects.get(id=id)
        print(contract)
        contract_updated = ContractSerializer(contract, data=request.data)
        print(contract_updated)
        if contract_updated.is_valid():
                contract_updated.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(contract_updated.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, formatters=None):
        id = int(request.GET.get('id'))
        init_table =  Contract.objects.filter(id=id)[:]
        for row in init_table:
            print(row)
            row.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#체결된 계약
class Contractlist(APIView):
    def post(self,request,formatter=None):
        print(request.data)
        contract_serializer = ContractSerializer(data=request.data) #Request의 data를 UserSerializer로 변환
        print(contract_serializer)
        if contract_serializer.is_valid():
            contract_serializer.save() #UserSerializer의 유효성 검사를 한 뒤 DB에 저장
            return Response(contract_serializer.data, status=status.HTTP_201_CREATED) #client에게 JSON response 전달
        else:
            return Response(contract_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def get(self,request,formatter=None):
        # print(request)
        email = request.GET.get('email',"")
        job = request.GET.get('job',"")
        # print(request.data)
        # print(r_data)
        # if job == 'farmer':
        contract = Contract.objects.filter(seller_email=email, seller_confirmed=True) | Contract.objects.filter(buyer_email=email, seller_confirmed=True)
        #     serializer = ContractSellerPreviewSerializer(contract, many=True)
        # else:
        #     contract = Contract.objects.filter(buyer_email=email, buyer_confirmed=True)
        serializer = ContractPreviewSerializer(contract, many=True)
        return Response(serializer.data)    

class Contract_unconfirmed(APIView):
    def get(self,request,formatter=None):
        # print(request)
        email = request.GET.get('email',"")
        posiotion = request.GET.get('position',"seller")
        # print(request.data)
        # print(r_data)
        if posiotion == 'seller':
            contract = Contract.objects.filter(seller_email=email, seller_confirmed=False)
            serializer = ContractPreviewSerializer(contract, many=True)
        else:
            contract =  Contract.objects.filter(buyer_email=email, seller_confirmed=False)
            serializer = ContractPreviewSerializer(contract, many=True)
        #     contract = Contract.objects.filter(buyer_email=email, buyer_confirmed=False)
        #     serializer = ContractBuyerPreviewSerializer(contract, many=True)
        return Response(serializer.data)    