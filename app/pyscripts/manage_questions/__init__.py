import hashlib
from supabase import create_client, Client
import random
import re
import json

API_URL = "https://vzvimxkzvvjyohbeodlq.supabase.co"
API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InZ6dmlteGt6dnZqeW9oYmVvZGxxIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY2MjI3NzEwNiwiZXhwIjoxOTc3ODUzMTA2fQ.vIPGMLpxL5Gnv5aLrI4_1CJvCGq3-aO-BPu9ll_s3gU"

supabase: Client = create_client(API_URL, API_KEY)