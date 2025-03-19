import os
import json
import requests
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from django.conf import settings

SCOPES = [
    "https://www.googleapis.com/auth/drive",
    "https://www.googleapis.com/auth/userinfo.email",
    "https://www.googleapis.com/auth/userinfo.profile",
    "openid"
]

def list_files():
    try:
        # Build the credentials correctly
        creds = Credentials(
            token=None,
            refresh_token=settings.GOOGLE_REFRESH_TOKEN,
            token_uri=settings.TOKEN_URI,
            client_id=settings.GOOGLE_CLIENT_ID,
            client_secret=settings.GOOGLE_CLIENT_SECRET,
            scopes=SCOPES
        )

        # Refresh token
        creds.refresh(Request())

        # Build Drive API service
        service = build("drive", "v3", credentials=creds)

        # Call Drive API
        results = service.files().list(pageSize=10).execute()
        return results.get("files", [])
    
    except Exception as e:
        return {"error": str(e)}


def upload_file_to_drive(file_obj, token):
    try:
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
    except Exception as e:
        return {"error": str(e)}

def download_file_from_drive(file_id, token):
    try:
        headers = {
            "Authorization": f"Bearer {token}"
        }
        url = f"https://www.googleapis.com/drive/v3/files/{file_id}?alt=media"
        response = requests.get(url, headers=headers)

        return {
            "status_code": response.status_code,
            "content": response.content if response.status_code == 200 else None  # Return raw content
        }
    except Exception as e:
        return {"error": str(e)}
