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
from django.urls import path

app_name = 'category'
urlpatterns = [
    # path('potato_data_insert/', views.DataInsert),
    path('carrot_price/', views.CarrotRealPrice.as_view()),
    path('seoul_price/', views.SeoulItemPrice.as_view()),
    path('pusan_price/', views.PusanItemPrice.as_view()),
    path('daegu_price/', views.DaeguItemPrice.as_view()),
    path('gwanju_price/', views.GwanjuItemPrice.as_view()),
    path('daejun_price/', views.DaejunItemPrice.as_view()),
###API    
    path('seoul_price_api/', views.SeoulItemAPIPrice.as_view()),
    path('daegu_price_api/', views.DaeguItemAPIPrice.as_view()),
    path('pusan_price_api/', views.PusanItemAPIPrice.as_view()),
    path('daejun_price_api/', views.DaejunItemAPIPrice.as_view()),
    path('gwanju_price_api/', views.GwanjuItemAPIPrice.as_view()),
]
