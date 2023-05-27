from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from url.views import UrlDetailViewSet

router = DefaultRouter()
router.register(r'url_detail',viewset=UrlDetailViewSet)

urlpatterns = [
    path('',include(router.urls))

]