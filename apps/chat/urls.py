from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.ChatTestView.as_view(), name='chat_test'),
]
