from django.urls import path

from users import views
from users.views import *

app_name = "users"

urlpatterns = [
    path("", views.UsersView.as_view()),

]