from django.urls import path

from users import views
from users.views import *

app_name = "users"

urlpatterns = [
    path("", views.SignUpView.as_view()), #sign-up
    path("me/", views.MeView.as_view()), #only my-info
    path("login/", views.LoginView.as_view()), #login
    path("<int:pk>/", views.DetailView.as_view()), #user-profile (only admin)

]