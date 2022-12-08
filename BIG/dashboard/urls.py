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
    path('', RedirectView.as_view(url='notice/', permanent=False), name='index'),
    path('notice/', views.notice, name='site_Notice'),
    path('QnA/', views.qna, name='site_QnA'),
    path('<int:id>/', views.detail, name='detail'),
    path('notice/new/', views.write_notice, name='create_notice'),
    path('QnA/new/', views.write_question, name='create_question'),
]