from django.urls import path
from . import views


# valid routes for Blog app
urlpatterns = [
  
    path('expenses1', views.expenses1, name="expenses1"),
    path('add-expense', views.add_expense, name="add-expenses"),
    path('register', views.registerPage, name="register"),
    path('login', views.loginPage, name="login"),
    path('logout', views.logoutUser, name="logout"),
]
