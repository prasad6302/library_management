from django.urls import path
from .views import user_login, register_student, user_logout

urlpatterns = [
    path("login/", user_login, name="login"),
    path("register/", register_student, name="register"),
    path("logout/", user_logout, name="logout"),
]
