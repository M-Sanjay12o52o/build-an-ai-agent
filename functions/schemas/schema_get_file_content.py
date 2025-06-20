from google.genai import types

schema_get_file_content = types.FunctionDeclaration(
  name="get_file_content",
  description="List files in the specified directory along with their sizes, constrained to the working directory.",
  parameters=types.Schema(
    type=types.Type.OBJECT,
    properties={
      "directory": types.Schema(
        type=types.Type.STRING,
        description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself."
      ),
    },
  ),
)