import os

# helpful standard library functions:
# os.path.abspath(): Get an absolute path from a relative path - NOT USED
# os.path.join(): Join two paths together safely (handles slashes) - USED ONCE
# .startswith(): Check if a string starts with a substring - NOT USED
# os.path.isdir(): Check if a path is a directory - USED TWICE
# os.listdir(): List the contents of a directory - USED ONCE
# os.path.getsize(): Get the size of a file - USED ONCE
# os.path.isfile(): Check if a path is a file - NOT USED
# .join(): Join a list of strings together with a separator - DON'T KNOW

def get_files_info(working_directory, directory=None):
  try:
    # if the `directory` argument is outside the `working_directory`
    # return a string with an error:
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
