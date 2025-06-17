import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

model = "gemini-2.0-flash-001"
contents = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."

if len(sys.argv) < 2: 
  print("Error: Prompt not provided")
  sys.exit(1)

user_prompt = sys.argv[1]

verbose = "--verbose" in sys.argv

messages = [
  types.Content(role="user", parts=[types.Part(text=user_prompt)]),
]

# response = client.models.generate_content(model=model, contents=contents)
# response = client.models.generate_content(model=model, contents=user_prompt)

response = client.models.generate_content(model=model, contents=messages)

prompt_tokens = response.usage_metadata.prompt_token_count
response_tokens = response.usage_metadata.candidates_token_count

# print("sys.argv:", sys.argv)

if (verbose):
  print("User prompt:", {user_prompt})
  print("Prompt tokens:", {prompt_tokens})
  print("Response tokens:", {response_tokens})
else :
  print(response.text)



