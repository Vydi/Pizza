from django.urls import path
from . import views


urlpatterns = [
    path('', views.MenuView.as_view(), name='index'),
    path('<str:slug>/', views.Detail_Pizza.as_view(), name='details'),
]
