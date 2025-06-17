from functions.get_files_info import get_files_info
import os

# Create a new tests.py file in the root of your project.
  # When executed directly, it should:
    # run `get_files_info("calculator", ".")` and print the result to the console.
    # run `get_files_info("calculator", "pkg")` and print the result to the console.
    # run `get_files_info("calculator", "/bin")` and print the result to the 
    # console (this should return an error string)
    # run `get_files_info("calculator", "../")` and print the result to the console
    # (this should return an error string)

working_directory = os.path.realpath("calculator")

result1 = get_files_info(working_directory, "calculator")
print(result1)

result2 = get_files_info(working_directory, "calculator/pkg")
print(result2)

result3 = get_files_info(working_directory, "/bin")
print(result3)

result4 = get_files_info(working_directory, "calculator/../")
print(result4)
