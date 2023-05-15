from django.urls import path, include
from .views import UBA_ViewSet, TransactionViewSet
from rest_framework import routers

router = routers.DefaultRouter()
app_name = 'api'

router.register('users', UBA_ViewSet, 'users')

urlpatterns = router.urls
