from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from .models import *
from .forms import *

# Create your views here.
def notice(request):
    search_key = request.GET.get('keyword','')
    post_list = Notice.objects.all()
    if search_key:
        post_list=post_list.filter(title__icontains=search_key)
    post_count = Notice.objects.count()
    context = {'post_all': post_list, 'post_count':post_count}
    return render(request, 'dashboard/notice.html', context)
def qna(request):
    search_key = request.GET.get('keyword','')
    post_list = Qna.objects.all()
    if search_key:
        post_list=post_list.filter(title__icontains=search_key)
    context = {'post_all': post_list}
    return render(request, 'dashboard/QnA.html', context)
def write_notice(request):
    if request.method=='POST':
        form = NoticeModelForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            # post = Post.objects.create(**form.cleaned_data)
            post = form.save()
            return redirect('../')
    else:
       form = NoticeModelForm()
       return render(request, 'dashboard/post_form.html',{'form':form})
def write_question(request):
    if request.method=='POST':
        form = NoticeModelForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            # post = Post.objects.create(**form.cleaned_data)
            post = form.save()
            return redirect('../')
    else:
       form = NoticeModelForm()
       return render(request, 'dashboard/post_form.html',{'form':form})
def detail(request, id):
    post = get_object_or_404(Notice, id=id)
    context = {'post':post}
    return render(request, 'dashboard/detail.html',context)