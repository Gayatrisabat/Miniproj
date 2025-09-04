import firebase_admin
from firebase_admin import credentials, firestore
import os

# Build absolute path to the JSON file
BASE_DIR = os.path.dirname(os.path.dirname(__file__))  # goes from database/ → backend/
json_path = os.path.join(BASE_DIR, "")

cred = credentials.Certificate(json_path)
firebase_admin.initialize_app(cred)

db = firestore.client()

#finlearn-46624-firebase-adminsdk-fbsvc-03eaf57778