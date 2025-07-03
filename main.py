import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from system_prompt import system_prompt
from functions.tool_schemas import available_function
from functions.call_function import call_function

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

# - [ ] Back in your `generate_content` function, instead of simply printing the name of the function the LLM decides to call, use `call_function`.
"""
- The `types.Content` that we return from `call_function` should have a `.parts[0].function_response.response` within.
- If it doesn't, `raise` a fatal exception of some sort.
- If it does, and `verbose` was set, print the result of the function call like this:
```
print(f"-> {function_call_result.parts[0].function_response.resopnse}")
```
"""

# - [ ] Test your program. You should now be able to execute each function given a prompt that asks for it. Try some different prompets and use the `--verbose` flag to make sure all the function work.
"""
- List the directory contents.
- Get a file's contents
- Write file contents (don't overwrite anything important, maybe create a new file)
- Execute the calculator app's tests (`tests.py`)
"""

response = client.models.generate_content(
  model=model, 
  contents=messages, 
  config=types.GenerateContentConfig(
    tools=[available_function],
    system_instruction=system_prompt
))

prompt_tokens = response.usage_metadata.prompt_token_count
response_tokens = response.usage_metadata.candidates_token_count

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

if function_call_part:
  function_call_result = call_function(function_call_part, verbose=verbose) 
  if function_call_result.parts[0].function_response.response:
    if verbose:
      print(f"-> {function_call_result.parts[0].function_response.response}")
  else:
    raise ValueError("Function response is empty or None.")
else:
  print("Response:", response.text) 


