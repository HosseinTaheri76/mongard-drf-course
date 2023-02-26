from django.urls import path

from . import views

app_name = 'home'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('questions/', views.QuestionView.as_view(), name='questions'),
    path('questions/<int:pk>/', views.QuestionView.as_view(), name='question_rud'),
]
