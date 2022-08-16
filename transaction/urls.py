from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path("home", views.index, name="index"),
    path("sign_up", views.sign_up, name="sign_up"),
    path('income/', views.income, name='income'),
    path("income/add", views.add_one, name="add_one"),
    path('expense/', views.expense, name='expense'),
    path("expense/add", views.add_two, name="add_two"),
]
