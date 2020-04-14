from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'regions', views.RegionsViewSet)
router.register(r'currencies', views.CurrenciesViewSet)
router.register(r'accounts', views.AccountsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
