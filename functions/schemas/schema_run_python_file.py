from google.genai import types

schema_run_python = types.FunctionDeclaration(
  name="run_python_file",
  description="Execute a Python file located in the working directory or a subdirectory.",
  parameters=types.Schema(
    type=types.Type.OBJECT,
    properties={
      "file_path": types.Schema(
        type=types.Type.STRING,
        description="Path to the Python file to execute, relative to the working directory. Example: 'main.py'",
      ),
    },
    required=["file_path"]
  ),
)
