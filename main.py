import os
from dotenv import load_dotenv
from google import genai
import sys

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
user_input = sys.argv[1]

if not user_input:
    sys.exit(1)
try:
    returned_value = client.models.generate_content(model = "gemini-2.0-flash-001", contents = f"{user_input}")
except Exception as e:
    raise e

print(returned_value.text)
