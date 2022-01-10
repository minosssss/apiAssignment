

from django.urls import path

from accountBook import views
from accountBook.views import *

app_name = "users"

urlpatterns = [
    path("", views.PaymentView.as_view()),
    path("record/", views.RecordView.as_view()),
]