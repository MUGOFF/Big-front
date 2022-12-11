from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.core.paginator import Paginator
from .models import *
from .forms import *

# Create your views here.
def notice(request, page=1):
    search_key = request.POST.get('keyword','')
    post_list = Notice.objects.all().order_by('-id')
    if search_key:
        post_list=post_list.filter(title__icontains=search_key)
        post_count = post_list.count()
    post_count = post_list.count()
    paginator = Paginator(post_list,10)
    post_list = paginator.page(page)
    print(post_list)
    page_num = post_count//10
    if post_count%10:
        page_num+=1
    context = {'post_all': post_list, 'post_count':post_count, 'page_num':range(1,page_num+1), 'page':page}
    return render(request, 'dashboard/notice.html', context)


def qna(request, page=1):
    search_key = request.POST.get('keyword','')
    post_list = Question.objects.all()
    if search_key:
        post_list=post_list.filter(title__icontains=search_key)
        post_count = post_list.count()
    post_count = post_list.count()
    paginator = Paginator(post_list,10)
    post_list = paginator.page(page)
    print(post_list)
    page_num = post_count//10
    if post_count%10:
        page_num+=1
    context = {'post_all': post_list,'post_count':post_count, 'page_num':range(1,page_num+1),'page':page}
    return render(request, 'dashboard/QnA.html', context)


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
def write_question(request):
    if request.method=='POST':
        form = QnAModelForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            # post = Post.objects.create(**form.cleaned_data)
            post = form.save()
            return redirect('../')
    else:
       form = QnAModelForm()
       return render(request, 'dashboard/post_form.html',{'form':form})
   

def notice_view(request, id):
    post = get_object_or_404(Notice, id=id)
    context = {'post':post}
    return render(request, 'dashboard/notice_detail.html',context)
def question_viw(request, id):
    post = get_object_or_404(Question, id=id)
    context = {'post':post}
    return render(request, 'dashboard/detail.html',context)