
from django.urls import path
from rest_framework.routers import DefaultRouter
from accountBook.views import RecordViewSet, PaymentViewSet

app_name = "assets"

router = DefaultRouter()
router.register(r'records', RecordViewSet, basename='Record')
router.register(r'payments', PaymentViewSet, basename='Payment')

urlpatterns = router.urls

