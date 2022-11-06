from django.urls import path
from . import views

#URL goes here

urlpatterns = [
    path('', views.home, name='home'),
    path('update/<str:id>/', views.update_tast, name='update'),
    path('delete/<str:id>/', views.delete_tast, name='delete'),
]