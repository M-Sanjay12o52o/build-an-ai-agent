import os
import subprocess
from google.genai import types
from config import MAX_CHARS 

def run_python_file(working_directory, file_path):
  working_directory = os.path.abspath(working_directory)
  abs_path = os.path.abspath(os.path.join(working_directory, file_path))

  # if the file_path is outside of the `working_directory`, return a string with an error:
  if not os.path.commonpath([working_directory, abs_path]) == working_directory:
      return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

  exists = os.path.exists(abs_path)

  # if the `file_path` doesn't exist, return an error string:
  if not exists: 
    return f'Error: File "{file_path}" not found.'
    
  # if the file doesn't end with ".py", return an error string:
  # to do this we first need to get the file name from the file_path
  filename = file_path
  root, ext = os.path.splitext(filename)
  if ext != ".py":
    return f'Error: "{file_path}" is not a Python file.'

  # Use `subprocess.run` function to execute the Python file
    # set a timeout of 30 seconds to prevent infinite execution
    # Try to execute the Python file safely
  try:
      # Run the Python file using subprocess with:
      # - capture_output=True: to collect both stdout and stderr
      # - text=True: to get output as strings (not bytes)
      # - timeout=30: to prevent the process from hanging forever
      # - cwd=working_directory: to ensure the script runs in the correct directory
      result = subprocess.run(
         ["python3", abs_path],
         capture_output=True,
         text=True,
         timeout=30,
         cwd=working_directory
      ) 

      output = ""

      # If there's output to stdout, include it
      if result.stdout:
         output += f"STDOUT:\n{result.stdout}"

      # If there's output to stderr, include it
      if result.stderr:
         output += f"STDERR:\n{result.stderr}"

      # If the script exited with an error (non-zero exit code), report it
      if result.returncode:
         output += f"\nProcess exited with code {result.returncode}"

      # If no output was produced at all, return a fallback message
      if not output.strip():
         return "No output produced"

      # Otherwise, return the full formatted output
      return output.strip()

  # Catch any unexpected exceptions (e.g., permission issues, file not executable)
  except Exception as e:
      return f'Error: executing Python file: {e}'



result = run_python_file("calculator", "main.py")
print(result)
print("\n")

result_two = run_python_file("calculator", "tests.py")
print(result_two)
print("\n")

# (this should return an error)
result_three = run_python_file("calculator", "../main.py") 
print(result_three)
print("\n")

# (this should return an error)
result_four = run_python_file("calculator", "nonexistent.py") 
print(result_four)
print("\n")

# (this should return an error)
result_five = run_python_file("calculator", "lorem.txt") 
print(result_five)
print("\n")


schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a Python file within the working directory and returns the output from the interpreter.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the Python file to execute, relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(
                    type=types.Type.STRING,
                    description="Optional arguments to pass to the Python file.",
                ),
                description="Optional arguments to pass to the Python file.",
            ),
        },
        required=["file_path"],
    ),
)










