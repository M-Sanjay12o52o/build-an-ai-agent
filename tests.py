# from functions.get_files_info import get_files_info
import os
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file

working_directory = os.path.realpath("calculator")


# run_python_file tests

result = run_python_file("calculator", "main.py")
print(result)
print("\n")

result_one = run_python_file("calculator", "tests.py")
print(result_one)
print("\n")


# (this should return an error)
result_two = run_python_file("calculator", "../main.py") 
print(result_two)
print("\n")


# (this should return an error)
result_three = run_python_file("calculator", "nonexistent.py") 
print(result_three)
print("\n")




# write_file tests

# result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
# print(result)

# result_one = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
# print(result_one)

# result_two = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
# print(result_two)

# update your tests.py file. Remove all the calls to `get_files_info`, and instead
# test `get_file_content("calculator", "lorem.txt")`. Ensure that it 
# truncates properly.
# result =  get_file_content(working_directory, "lorem.txt")
# print(result)

# result1 = get_file_content(working_directory, "main.py")
# print(result1)

# result2 = get_file_content(working_directory, "pkg/calculator.py")
# print(result2)

# result3 = get_file_content(working_directory, "bin/cat")
# print(result3)

# # Create a new tests.py file in the root of your project.
#   # When executed directly, it should:
#     # run `get_files_info("calculator", ".")` and print the result to the console.
#     # run `get_files_info("calculator", "pkg")` and print the result to the console.
#     # run `get_files_info("calculator", "/bin")` and print the result to the 
#     # console (this should return an error string)
#     # run `get_files_info("calculator", "../")` and print the result to the console
#     # (this should return an error string)

# working_directory = os.path.realpath("calculator")

# result1 = get_files_info(working_directory, "calculator")
# print(result1)

# result2 = get_files_info(working_directory, "calculator/pkg")
# print(result2)

# result3 = get_files_info(working_directory, "/bin")
# print(result3)

# result4 = get_files_info(working_directory, "calculator/../")
# print(result4)


