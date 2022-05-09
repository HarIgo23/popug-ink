from django.urls import path
from .views import login, authorize

urlpatterns = [
    path('login/', login),
    path('account/', authorize),
]
