from google.genai import types

schema_get_file_content = types.FunctionDeclaration(
  name="get_file_content",
  description="Read the contents of a file in the specified directory, constrained to the working directory.",
  parameters=types.Schema(
    type=types.Type.OBJECT,
    properties={
      "directory": types.Schema(
        type=types.Type.STRING,
        description="The directory containing the file to read, relative to the working directory. Defaults to working directory if not provided.",
      ),
      "file_path": types.Schema(
        type=types.Type.STRING,
        description="The relative path to the file to read inside the specified directory.",
      ),
    },
    required=["file_path"]
  ),
)
