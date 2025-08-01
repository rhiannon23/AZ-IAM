import requests
from msal import ConfidentialClientApplication

from dotenv import load_dotenv
import os

env_path = os.path.join(os.path.dirname(__file__), "..", ".env")
load_dotenv(dotenv_path=env_path)

TENANT_ID = os.getenv("TENANT_ID")
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

AUTHORITY = f"https://login.microsoftonline.com/{TENANT_ID}"
SCOPE = ["https://graph.microsoft.com/.default"]

def get_access_token():
    app = ConfidentialClientApplication(
        CLIENT_ID,
        authority=AUTHORITY,
        client_credential=CLIENT_SECRET,
    )
    result = app.acquire_token_for_client(scopes=SCOPE)
    if "access_token" in result:
        return result["access_token"]
    else:
        raise Exception(f"Auth failed: {result}")

def get_users():
    token = get_access_token()
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get("https://graph.microsoft.com/v1.0/users", headers=headers)
    return response.json()
