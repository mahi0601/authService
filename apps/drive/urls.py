from django.urls import path
from .views import UploadFileView, DownloadFileView
from .views import ListDriveFilesView

urlpatterns = [
    path('upload/', UploadFileView.as_view(), name='upload_file'),
    path('download/', DownloadFileView.as_view(), name='download_file'),
     path('list/', ListDriveFilesView.as_view(), name='list_drive_files'), 
]
