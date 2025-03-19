from rest_framework.views import APIView
from rest_framework.response import Response
from .services.drive_service import upload_file_to_drive, download_file_from_drive

class UploadFileView(APIView):
    def post(self, request):
        file = request.FILES.get('file')
        token = request.headers.get('Authorization', '').split(" ")[1]
        if not file:
            return Response({'error': 'No file uploaded'}, status=400)
        upload_result = upload_file_to_drive(file, token)
        return Response(upload_result)

class DownloadFileView(APIView):
    def get(self, request):
        file_id = request.GET.get('file_id')
        token = request.headers.get('Authorization', '').split(" ")[1]
        result = download_file_from_drive(file_id, token)
        return Response(result)
