from django.urls import path
from .views import UploadFileView, DownloadFileView

urlpatterns = [
    path('upload/', UploadFileView.as_view(), name='upload_file'),
    path('download/', DownloadFileView.as_view(), name='download_file'),
]
