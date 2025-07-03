from google.genai import types
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.get_files_info import get_files_info
from functions.run_python_file import run_python_file

function_map = {
    "get_file_content": get_file_content,
    "write_file": write_file,
    "get_files_info": get_files_info,
    "run_python_file": run_python_file,
}


def call_function(function_call_part, verbose=False):
  if verbose:
    print(f"Calling function: {function_call_part.name}({function_call_part.args})")
  else:
    print(f" - Calling function: {function_call_part.name}")

  function_name = function_call_part.name

  if function_name:
    function = function_map.get(function_name)
    if function:
      try:
        function_result = function(**function_call_part.args)
        if verbose:
          print(f"Function {function_name} returned: {function_result}")
          print(f"[DEBUG] Returning from {function_name}: {repr(function_result)}")
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response=function_result
                )
            ],
        )
      except Exception as e:
        print(f"Error calling function {function_name}: {e}")
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": str(e)},
                )
            ],
        )
    else:
      print(f"Function {function_name} not found.")
  else:
    return types.Content(
    role="tool",
    parts=[
        types.Part.from_function_response(
            name=function_name,
            response={"error": f"Unknown function: {function_name}"},
        )
    ],
)