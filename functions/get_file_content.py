import os

def get_file_content(working_directory, file_path):
  try:
    # if the file_path is outside the `working_directory`
    # return a string with an error:
    # abs_file_path = os.path.join(working_directory, file_path)

    working_directory = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    # if not os.path.commonpath([working_directory, abs_file_path]) == working_directory:
    if not os.path.commonpath([working_directory, abs_file_path]) == working_directory:
      return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    else:
      # if the file_path is not a file, again, return an error string 
      if not os.path.isfile(abs_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
      else:
        # read the file and return its contents as a string.
        # if the file is longer than `10000` characters, truncate it to
        # `10000` characters and append this message to the end:
        # `[...File "{file_path} truncated at 10000 characters"]`
        MAX_CHARS = 10000

        with open(abs_file_path, "r") as f:
          file_content_string = f.read(MAX_CHARS)
          remaining = f.read(1)

          if remaining:
            file_content_string += f'\n[...File "{file_path} truncated at {MAX_CHARS} characters"]'
          return file_content_string 

  except Exception as e:
      return f'Error: {str(e)}'


