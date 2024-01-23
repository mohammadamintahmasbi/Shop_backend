from django.urls import path
from .views import CreateUserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = "users"

urlpatterns = [
    path(r"create/", view=CreateUserView.as_view(), name="user_create"),
    path(r"token/", view=TokenObtainPairView.as_view(), name="user_token"),
    path(r"token/refresh/", view=TokenRefreshView.as_view(), name="user_token_refresh")
]