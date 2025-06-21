from google.genai import types

schema_write_file = types.FunctionDeclaration(
  name="write_file",
  description="The path to the file to write, relative to the working directory. Example: 'main.txt'.",
  parameters=types.Schema(
    type=types.Type.OBJECT,
    properties={
      "file_path": types.Schema(
        type=types.Type.STRING,
        description="The directory where the file will be written, relative to the working directory. If not provided, defaults to the working directory itself.",
      ),
      "content": types.Schema(
        type=types.Type.STRING,
        description="The content to write to the file. If the file already exists, it will be overwritten.",
      )
    },
    required=["file_path", "content"]
  ),
)