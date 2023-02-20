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
from rest_framework import routers
from django.urls import path, include

router = routers.DefaultRouter()
router.register('user', views.UserViewSet)

app_name = 'account'
urlpatterns = [
    # path('', RedirectView.as_view(url='notice/', permanent=False), name='index'),
    path('', include(router.urls)),
    path('UserPreview/', views.UserProfile.as_view()),
    path('Contract_list/', views.Contractlist.as_view()),
    path('Contract_sign/', views.Contract_doc.as_view()),
    path('Contract_inprogress/', views.Contract_unconfirmed.as_view()),
    path('updateuser/', views.UserUpdateView.as_view()),
    # path('my_contract/', views.Contractlist.as_view()),
]
