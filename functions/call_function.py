from google.genai import types
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.get_files_info import get_files_info
from functions.run_python_file import run_python_file
import inspect

function_map = {
    "get_file_content": get_file_content,
    "write_file": write_file,
    "get_files_info": get_files_info,
    "run_python_file": run_python_file,
}

# Questions:
# 1. What is the dictionary of keyword arguments. ( Because we need to manually add the "working_directory" argument to it )
  # The syntax to pass a dictionary into a function using keyword arguments is `some_function(**some_args)`


# - [ ] Create a new function that will handle the abstract task of calling one of our four functions.
"""
`function_call_part` is a types.FunctionCall that most importantly has:
- A `.name` property (the name of the function, a `string`)
- A `.args` property (a dictionary of named arguments to the function)
""" 
def call_function(function_call_part, verbose=False):
  # - [x] 1. If `verbose` is specified, print the function name and args:
  if verbose:
    print(f"Calling function: {function_call_part.name}({function_call_part.args})")
  # - [x] 2. Otherwise, just print the name:
  else:
    print(f" - Calling function: {function_call_part.name}")

  # - [ ] Based on the name, actually call the function and capture the result.
  # - [ ] Be, sure to manually add the "working_directory" argument to the dictionary of keyword arguments, because the LLM doesn't control that one. The working directory should be `./calculator`
  # - [ ] The syntax to pass a dictionary into a function using keyword arguments is `some_function(**some_args)`
  function_name = function_call_part.name

  if function_name:
    args = dict(function_call_part.args)
    args["working_directory"] = "./calculator"

    function = function_map.get(function_name)
    if function:
      sig = inspect.signature(function)
      if "directory" in sig.parameters:
        if "directory" not in args or args["directory"] in [None, ".", "./"]:
          args["directory"] = "./calculator"
      else:
        args.pop("directory", None)

      try:
        function_result = function(**args)
        if verbose:
          print(f"Function {function_name} returned: {function_result}")
          print(f"[DEBUG] Returning from {function_name}: {repr(function_result)}")
        # - [ ] Return `types.Content` with a `from_function_response` describing the result of the function call:
        """
        return types.Content(
          role="tool",
          parts=[
              types.Part.from_function_response(
                name=function_name,
                response={"result": funciton_result}
              )
          ],
        )
        """
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"result": function_result}
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
  # - [ ] If the function name is invalid, return a `types.Content` that explains the error:
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
  



