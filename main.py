import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

user_input = sys.argv[1]

if not user_input:
    sys.exit(1)

messages = [types.Content(role="user", parts = [types.Part(text=user_input)])]
to_show_user = ""

try:
    returned_value = client.models.generate_content(model = "gemini-2.0-flash-001", contents = messages)
    to_show_user += returned_value.text
except Exception as e:
    raise e


if sys.argv[2] and sys.argv[2] == "--verbose":
    to_show_user += f"""\nUser prompt: {user_input}\nPrompt tokens: {returned_value.usage_metadata.prompt_token_count}\nResponse tokens: {returned_value.usage_metadata.total_token_count}
        """
    
print(to_show_user)
