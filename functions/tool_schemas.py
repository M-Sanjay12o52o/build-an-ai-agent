# functions/tool_schemas.py
from google.genai import types
from functions.schemas.schema_get_files_info import schema_get_files_info
from functions.schemas.schema_run_python_file import schema_run_python
from functions.schemas.schema_write_file import schema_write_file
from functions.schemas.schema_get_file_content import schema_get_file_content

available_function = types.Tool(
  function_declarations=[
    schema_get_files_info,
    schema_run_python,
    schema_write_file,
    schema_get_file_content,
  ]
)