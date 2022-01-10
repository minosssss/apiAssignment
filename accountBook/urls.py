
from django.urls import path
from rest_framework.routers import DefaultRouter
from accountBook.views import RecordViewSet

app_name = "assets"

router = DefaultRouter()
router.register("", RecordViewSet)

urlpatterns = router.urls

# urlpatterns = [
#     path("", views.PaymentView.as_view()),
#     path("record/", views.RecordView.as_view()),
# ]