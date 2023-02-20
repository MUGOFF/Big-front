from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.core.paginator import Paginator
from .models import *
from .forms import *
from .serializers import *
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

class NoticeList(APIView):
    def get(self,request, formatter=None):
        # pages = int(request.GET.get('page',1))
        notices = Notice.objects.all()
        # paginator = Paginator(notices,10)
        # post_list = paginator.page(pages)
        serializer = NoticeListSerializer(notices, many=True)
        return Response(serializer.data)
class NoticeDetail(APIView):
    def get(self,request, formatter=None):
        id = int(request.GET.get('id',1))
        notices = Notice.objects.filter(id=id)
        serializer = NoticeContentSerializer(notices, many=True)
        return Response(serializer.data)
class QnaList(APIView):
    def get(self,request, formatter=None):
        # pages = int(request.GET.get('page',1))
        notices = Question.objects.all()
        # paginator = Paginator(notices,10)
        # post_list = paginator.page(pages)
        serializer = QnaListSerializer(notices, many=True)
        return Response(serializer.data)
class QnaDetail(APIView):
    def get(self,request, formatter=None):
        id = int(request.GET.get('id',1))
        contest_list = Question.objects.filter(id=id)
        serializer = QnaContentSerializer(contest_list, many=True)
        return Response(serializer.data)
    def delete(self,request, formatter=None):
        id = int(request.GET.get('id',1))
        contest_list = Question.objects.filter(id=id)
        if contest_list != None: 
            contest_list.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    def post(self,request,formatter=None):
        serializer = QnaContentSerializer(data=request.data) #Request의 data를 UserSerializer로 변환
        if serializer.is_valid():
            serializer.save() #UserSerializer의 유효성 검사를 한 뒤 DB에 저장
            return Response(serializer.data, status=status.HTTP_201_CREATED) #client에게 JSON response 전달
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self,request,formatters=None):
        id = int(request.GET.get('id',1))
        contest_list = Question.objects.get(id=id)
        if contest_list != None: 
            update_content = QnaContentSerializer(contest_list, data=request.data)
            if update_content.is_valid():
                update_content.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
class AnswerView(APIView):
    def get(self, request, formatter=None):
        id = int(request.GET.get('id',1))
        Qu = Question.objects.get(id=id)
        answer_list = Answer.objects.filter(post=Qu)
        serializer = AnswerSerializer(answer_list, many=True)
        return Response(serializer.data)
        
# # Create your views here.
# def notice(request, page=1):
#     search_key = request.POST.get('keyword','')
#     post_list = Notice.objects.all().order_by('-id')
#     if search_key:
#         post_list=post_list.filter(title__icontains=search_key)
#         post_count = post_list.count()
#     post_count = post_list.count()
#     paginator = Paginator(post_list,10)
#     post_list = paginator.page(page)
#     print(post_list)
#     page_num = post_count//10
#     if post_count%10:
#         page_num+=1
#     context = {'post_all': post_list, 'post_count':post_count, 'page_num':range(1,page_num+1), 'page':page}
#     return render(request, 'dashboard/notice.html', context)


# def qna(request, page=1):
#     search_key = request.POST.get('keyword','')
#     post_list = Question.objects.all()
#     if search_key:
#         post_list=post_list.filter(title__icontains=search_key)
#         post_count = post_list.count()
#     post_count = post_list.count()
#     paginator = Paginator(post_list,10)
#     post_list = paginator.page(page)
#     print(post_list)
#     page_num = post_count//10
#     if post_count%10:
#         page_num+=1
    # context = {'post_all': post_list,'post_count':post_count, 'page_num':range(1,page_num+1),'page':page}
    # return render(request, 'dashboard/QnA.html', context)


# def write_notice(request):
#     if request.method=='POST':
#         form = NoticeModelForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             # post = Post.objects.create(**form.cleaned_data)
#             post = form.save()
#             return redirect('../')
#     else:
#        form = NoticeModelForm()
#        return render(request, 'dashboard/post_form.html',{'form':form})
# def write_question(request):
#     if request.method=='POST':
#         form = QnAModelForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             # post = Post.objects.create(**form.cleaned_data)
#             post = form.save()
#             return redirect('../')
#     else:
#        form = QnAModelForm()
#        return render(request, 'dashboard/post_form.html',{'form':form})
   

# def notice_view(request, id):
#     post = get_object_or_404(Notice, id=id)
#     context = {'post':post}
#     return render(request, 'dashboard/notice_detail.html',context)
# def question_viw(request, id):
#     post = get_object_or_404(Question, id=id)
#     context = {'post':post}
#     return render(request, 'dashboard/detail.html',context)