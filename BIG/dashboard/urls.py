"""BIG URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from . import views
from django.views.generic.base import RedirectView
from django.urls import path

app_name = 'dashboard'
urlpatterns = [
    # path('', RedirectView.as_view(url='notice/', permanent=False), name='index'),
    path('notices/', views.NoticeList.as_view()),
    path('notices_detail/', views.NoticeDetail.as_view()),
    path('questions/', views.QnaList.as_view()),
    path('qnas_detail/', views.QnaDetail.as_view()),
    path('answer_comment/', views.AnswerView.as_view()),
    # path('notice/', views.notice, name='site_Notice'),
    # path('notice/page=<int:page>/', views.notice, name='site_Notice_page'),
    # path('QnA/', views.qna, name='site_QnA'),
    # path('QnA/page=<int:page>/', views.qna, name='site_QnA_page'),
    # path('notice/<int:id>/', views.notice_view, name='notice_view'),
    # path('QnA/<int:id>/', views.question_viw, name='question_viw'),
    # # path('notice/new/', views.write_notice, name='create_notice'),
    # path('QnA/new/', views.write_question, name='create_question'),
]
