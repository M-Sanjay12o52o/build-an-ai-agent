import os
import subprocess

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
  try:
      result = subprocess.run(
         ["python3", abs_path],
         capture_output=True,
         text=True,
         timeout=30,
         cwd=working_directory
      ) 

      output = ""
      if result.stdout:
         output += f"STDOUT:\n{result.stdout}"
      if result.stderr:
         output += f"STDERR:\n{result.stderr}"
      if result.returncode:
         output += f"\nProcess exited with code {result.returncode}"
      if not output.strip():
         return "No output produced"
      return output.strip()

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













