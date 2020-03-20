from django.urls import path
from django.urls import include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register('statistic', views.StatisticViewSet, basename='statistic')
router.register('province', views.ProvinceViewSet, basename='province')
urlpatterns = [
    path('', include(router.urls))
]