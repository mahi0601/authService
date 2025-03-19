from django.urls import path
from .views import GoogleAuthInitView, GoogleAuthCallbackView,auth_home

urlpatterns = [
    path('', auth_home, name='auth_home'), 
    path('init/', GoogleAuthInitView.as_view(), name='google_auth_init'),
    path('callback/', GoogleAuthCallbackView.as_view(), name='google_auth_callback'),
]
