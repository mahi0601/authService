import os
import json
import requests
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from django.conf import settings


def list_files():
    creds = Credentials(
        token=settings.DRIVE_ACCESS_TOKEN,
        refresh_token=settings.GOOGLE_REFRESH_TOKEN,
        token_uri=settings.TOKEN_URI,
        client_id=settings.GOOGLE_CLIENT_ID,
        client_secret=settings.GOOGLE_CLIENT_SECRET,
        scopes=["https://www.googleapis.com/auth/drive"]
    )
    print("ACCESS TOKEN", settings.DRIVE_ACCESS_TOKEN)
    print("REFRESH TOKEN", settings.GOOGLE_REFRESH_TOKEN)
    print("CLIENT ID", settings.GOOGLE_CLIENT_ID)
    print("CLIENT SECRET", settings.GOOGLE_CLIENT_SECRET)
    print("TOKEN URI", settings.TOKEN_URI)

    # Ensure the access token is refreshed if expired
    if creds.expired and creds.refresh_token:
        creds.refresh(Request())

    service = build("drive", "v3", credentials=creds)
    results = service.files().list(pageSize=10).execute()
    return results.get("files", [])


def upload_file_to_drive(file_obj, token):
    headers = {
        "Authorization": f"Bearer {token}"
    }
    metadata = {
        "name": file_obj.name
    }
    files = {
        'metadata': ('metadata', json.dumps(metadata), 'application/json'),
        'file': (file_obj.name, file_obj.read())
    }
    response = requests.post(
        "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
        headers=headers,
        files=files
    )
    return response.json()


def download_file_from_drive(file_id, token):
    headers = {
        "Authorization": f"Bearer {token}"
    }
    url = f"https://www.googleapis.com/drive/v3/files/{file_id}?alt=media"
    response = requests.get(url, headers=headers)

    return {
        "status_code": response.status_code,
        "content": response.content.decode('utf-8') if response.status_code == 200 else None
    }
