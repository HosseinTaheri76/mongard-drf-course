from django.urls import path
from rest_framework.authtoken import views as auth_token
from rest_framework import routers

from . import views

app_name = 'accounts'

urlpatterns = [
    path('register/', views.UserRegister.as_view()),
    path('login/', auth_token.obtain_auth_token),
]

router = routers.SimpleRouter()
router.register('user', views.UserViewSet)
urlpatterns += router.urls
