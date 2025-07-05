import os
import sys
from google import genai
from google.genai import types
from dotenv import load_dotenv

from prompts import robot_system_prompt 
from system_prompt import system_prompt
from functions.tool_schemas import available_function
from functions.call_function import call_function
from functions.get_file_content import get_file_content
from config import MAX_CHARS


def main():
  load_dotenv()
  
  verbose = "--verbose" in sys.argv
  args = [arg for arg in sys.argv[1:] if not arg.startswith("--")]

  if not args:
    print("AI Code Assistant")
    print('\nUsage: python main.py "your prompt here" [--verbose]')
    print('Example: python main.py "How do I build a calculator app?"')
    sys.exit(1)

  api_key = os.environ.get("GEMINI_API_KEY")
  client = genai.Client(api_key=api_key)

  user_prompt = " ".join(args)

  if verbose:
    print(f"User prompt: {user_prompt}\n")

  messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
  ]

  get_file_content_result = get_file_content("./", "./calculator/pkg/calculator.py")

  print("\n---Start---\n")
  print("get_files_content_result")
  print(get_file_content_result)
  print("\n---End---\n")

  generate_content(client, messages, verbose)



def generate_content(client, messages, verbose):
  response = client.models.generate_content(
      model="gemini-2.0-flash-001", 
      contents=messages, 
      config=types.GenerateContentConfig(
        tools=[available_function], system_instruction=system_prompt
      )
    )

  if verbose:
    print("Prompt tokens:", response.usage_metadata.prompt_token_count)
    print("Response tokens:", response.usage_metadata.candidates_token_count)

  if not response.function_calls:
    return response.text  

  function_responses = []

  # Assignment
  # - [x] Create a loop that iterates at most 20 times (this will stop our agent from spinning its wheels forever).
  for i in range(20):
    # - [x] In each iteration, check the .candidates property of the response. It's a list of response variations, and in particular it contains the equivalent of "I want to call get_files_info...", so we need to add it to our conversation. Iterate over each candidate and add its .content to your messages list.
    for candidate in response.candidates:
      messages.append(candidate.content)

    # - [x] After each actual function call, append the returned types.Content to the messages as well. This is the equivalent of "Here's the result of get_files_info...".
    # - [x] After each iteration, if a function was called, you should iterate again (unless max iterations was reached). Otherwise, you should print the LLM's final response (the .text property of the response) and break out - this means the agent is done with the task! (or failed miserably, which happens as well)
        
    if not response.function_calls:
      print(response.text)
      break

    for function_call_part in response.function_calls:
      print("\n---Start---\n")
      print("function call from main")
      print("function_call_part: ", function_call_part)
      print("\n---End---\n")
      function_call_result = call_function(function_call_part, verbose)
      messages.append(function_call_result.parts[0]) 


    # - [x] This might already be happening, but make sure that with each call to client.models.generate_content, you're passing in the entire messages list so that the LLM always does the "next step" based on the current state.
    response = client.models.generate_content(
          model="gemini-2.0-flash-001", 
          contents=messages, 
          config=types.GenerateContentConfig(
            tools=[available_function], system_instruction=system_prompt
          )
        )


    if (
      not function_call_result.parts
      or not function_call_result.parts[0].function_response
    ):
      raise Exception("empty function call result")
    if verbose:
      print(f"-> {function_call_result.parts[0].function_response.response}")
    function_responses.append(function_call_result.parts[0])

  if not function_responses:
    raise Exception("no function responses generated, exiting.")

if __name__ == "__main__":
  main()









