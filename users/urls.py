from django.urls import path
from rest_framework.routers import DefaultRouter
from users.views import UsersViewSet

app_name = "users"

router = DefaultRouter()
router.register("", UsersViewSet)
urlpatterns = router.urls


# urlpatterns = [
#     path("", views.SignUpView.as_view()), #sign-up
#     path("me/", views.MeView.as_view()), #only my-info
#     path("login/", views.LoginView.as_view()), #login
#     path("<int:pk>/", views.DetailView.as_view()), #user-profile (only admin)
#
# ]