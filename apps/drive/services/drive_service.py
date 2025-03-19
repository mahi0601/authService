import requests
import json
# apps/drive/services/drive_service.py
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from django.conf import settings

def list_files():
    creds = Credentials(token=settings.DRIVE_ACCESS_TOKEN)
    service = build('drive', 'v3', credentials=creds)
    results = service.files().list(pageSize=10).execute()
    files = results.get('files', [])
    return files


def upload_file_to_drive(file_obj, token):
    headers = {"Authorization": f"Bearer {token}"}
    metadata = {'name': file_obj.name}
    files = {
        'metadata': ('metadata', json.dumps(metadata), 'application/json'),
        'file': (file_obj.name, file_obj.read())
    }
    response = requests.post(
        'https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart',
        headers=headers,
        files=files
    )
    return response.json()

def download_file_from_drive(file_id, token):
    headers = {"Authorization": f"Bearer {token}"}
    url = f'https://www.googleapis.com/drive/v3/files/{file_id}?alt=media'
    response = requests.get(url, headers=headers)
    return {
        'status_code': response.status_code,
        'content': response.content.decode('utf-8')
    }
