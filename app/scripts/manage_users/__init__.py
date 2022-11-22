import hashlib
from supabase import create_client, Client
import random
import re
from dotenv import load_dotenv
import os

load_dotenv()

# API url and key stored in .env file for security
API_URL = os.getenv("API_URL")
API_KEY = os.getenv("API_KEY")

supabase: Client = create_client(API_URL, API_KEY)