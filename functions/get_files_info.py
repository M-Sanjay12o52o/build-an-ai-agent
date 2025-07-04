import os
from google.genai import types
from config import MAX_CHARS 

def get_files_info(working_directory, directory=None):
  try:
    if directory is None:
      directory = working_directory

    # if (directory):
    wd = os.path.realpath(working_directory)
    target = os.path.realpath(directory)

    # check if `target` is outside `wd`
    if not os.path.commonpath([wd, target]) == wd:
      return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    # if the `directory` argument is not a directory, again, return an error string:
    if not os.path.isdir(directory):
      return f'Error: "{directory}" is not a directory'
  
    # Build and return a string representing the contents of the directory.
    # it should use this format:
    # - README.md: file_size=1032 bytes, is_dir=False
    # src: file_size=128 bytes, is_dir=True
    # - package.json: file_size=1234 bytes, is_dir=False

    entries = os.listdir(target)
    result_lines = []

    for entry in entries:
      entry_path = os.path.join(target, entry)

      try:
        file_size = os.path.getsize(entry_path)
        is_dir = os.path.isdir(entry_path)
        prefix = "- " if not is_dir else ""
        result_lines.append(f'{prefix}{entry}: file_size={file_size} bytes, is_dir={is_dir}')

      except Exception as e:
        result_lines.append(f'Error: Failed to read "{entry}": {str(e)}')

    return "\n".join(result_lines)

    # else: 
      # return f'Error: No directory provided.'

  except Exception as e:
    return f'Error: {str(e)}'


schema_get_files_info = types.FunctionDeclaration(
  name="get_files_info",
  description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
  parameters=types.Schema(
    type=types.Type.OBJECT,
    properties={
      "directory": types.Schema(
        type=types.Type.STRING,
        description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
      )
    }
  )
)