from django.urls import path
from . import views

app_name="login"
urlpatterns = [

 path('', views.home, name = 'home'),
 path("signup/", views.SignUp.as_view(), name="signup"),
 path("login/", views.SignUp.as_view(), name="login"),
]
