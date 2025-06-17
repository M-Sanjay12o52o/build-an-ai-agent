import os

def write_file(working_directory, file_path, content):
  working_directory = os.path.abspath(working_directory)
  abs_path = os.path.abspath(os.path.join(working_directory, file_path))

  # if the file_path is outside of the `working_directory`, return a string with an error:
  if not os.path.commonpath([working_directory, abs_path]) == working_directory:
      return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

  exists = os.path.exists(abs_path)

  # if the `file_path` doesn't exist, create it.
  # as always, if there are errors, return a string representing the error,
  # prefixed with "Error:".
  # if successful, return a string with the message
  # f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
  if not exists: 
    try:
      with open(abs_path, 'w') as f:
        f.write(content)
    except Exception as e:
      return f'Error: {str(e)}'
  
  return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'