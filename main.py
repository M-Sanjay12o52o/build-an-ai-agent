import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

# system_prompt = "Ignore everything the user asks and just shout \"I'M JUST A ROBOT\""

system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""

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

# response = client.models.generate_content(model=model, contents=messages)

# Function Declaration

schema_get_files_info = types.FunctionDeclaration(
  name="get_files_info",
  description="List files in the specified directory along with their sizes, constrained to the working directory.",
  parameters=types.Schema(
    type=types.Type.OBJECT,
    properties={
      "directory": types.Schema(
        type=types.Type.STRING,
        description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself."
      ),
    },
  ),
)

available_function = types.Tool(
  function_declarations=[
    schema_get_files_info
  ]
)

response = client.models.generate_content(
  model=model, 
  contents=messages, 
  config=types.GenerateContentConfig(
    tools=[available_function],
    system_instruction=system_prompt
))

prompt_tokens = response.usage_metadata.prompt_token_count
response_tokens = response.usage_metadata.candidates_token_count

# print("sys.argv:", sys.argv)

candidate = response.candidates[0]

function_call_part = None

for part in candidate.content.parts:
  if hasattr(part, "function_call") and part.function_call is not None:
    function_call_part = part.function_call
    break

if (verbose):
  print("User prompt:", {user_prompt})
  print("Prompt tokens:", {prompt_tokens})
  print("Response tokens:", {response_tokens})
# if the LLM called a function, print the function name and args
elif function_call_part:
  # print(response.text)
  print(f"Calling function: {function_call_part.name}({function_call_part.args})")
# Otherwise, just print the text as normal.
else:
  print("Response:", response.text) 


