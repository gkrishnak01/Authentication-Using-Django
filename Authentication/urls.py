from django.urls import path
from .views import signUp,login,home,logout

app_name = "Authentication"

urlpatterns = [
    path("signup",signUp,name="signup"),
    path("",login,name="login"),
    path("home",home,name="home"),
    path("logout",logout,name="logout")
]