from functions.run_python_file import run_python_file
# from config import WORKING_DIR as working_dir
from functions.get_file_content import get_file_content
# from config import MAIN_DIR as working_dir

working_dir = "./"


def test():
  result = run_python_file("calculator", "main.py")
  print("\n---Start---\n")
  print(result)
  print("\n---End---\n")
  print("\n")


  # result_one = run_python_file("calculator", "tests.py")
  # print(result_one)
  # print("\n")


  # # (this should return an error)
  # result_two = run_python_file("calculator", "../main.py") 
  # print(result_two)
  # print("\n")


  # # (this should return an error)
  # result_three = run_python_file("calculator", "nonexistent.py") 
  # print(result_three)
  # print("\n")

  # this works as expected
  # Case 1: Valid small file
  # print(get_file_content(working_dir, "small.txt"))

  # this works as expected
  # Case 2: Valid long file
  # print(get_file_content(working_dir, "long.txt"))

  # this works as expected
  # # Case 3: File doesn't exist
  # print(get_file_content(working_dir, "does_not_exist.txt"))

  # this works as expected
  # # Case 4: File outside working directory
  # print(get_file_content(working_dir, "../some_other_file.txt"))

  # this works fine
  # Case 5: Directory instead of file
  # print(get_file_content(working_dir, "subdir/nested.txt"))

  # this works fine
  # Case 6:
  # print("\n---Start---\n")
  # print(get_file_content(working_dir, "calculator/pkg/calculator.py"))
  # print("\n---End---\n")

if __name__ == "__main__":
  test()


"""
Questions: 

1. How is the get_file_content function supposed to work ?
Ans.  print(get_file_content(working_dir, "subdir/nested.txt")) - And it works as well.
      print(get_file_content(working_dir, "calculator/pkg/calculator.py")) - This too works fine.

2. With just this let's verify whether we can use the ai agent to update the code to fix bugs.
Ans.  In short it did not, but it did as for the specific path of the file where the changes needed to be made.
      And then it did tell us that it fixed it but it actually did not.

3. When we further pushed it to solve the problem, it further with this prompt `uv run main.py "i don't see no change and i can still see that 3 + 7 * 2 is resulting in 20 which it should not, the solution should actually be 17 as 7 * 2 = 14 + 3 = 17"`

  Traceback (most recent call last):
  File "/Users/msanjayachar/Desktop/workspace/code/courses/boot-dot-dev/build-an-ai-agent/main.py", line 102, in <module>
    main()
    ~~~~^^
  File "/Users/msanjayachar/Desktop/workspace/code/courses/boot-dot-dev/build-an-ai-agent/main.py", line 38, in main
    generate_content(client, messages, verbose)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/msanjayachar/Desktop/workspace/code/courses/boot-dot-dev/build-an-ai-agent/main.py", line 75, in generate_content
    function_call_result = call_function(function_call_part, verbose)
  File "/Users/msanjayachar/Desktop/workspace/code/courses/boot-dot-dev/build-an-ai-agent/functions/call_function.py", line 35, in call_function
    function_result = function_map[function_name](**args)
TypeError: run_python_file() got an unexpected keyword argument 'arguments'

    ~/De/w/c/cou/b/build-an-ai-agent  on   main !7 ?3      
  1. What does the above error exactly say ? 
    run_python_file() got an unexpected keyword argument 'arguments'


4. The agent is currently modifing the calculator/main.py code to return the result of print(3 + 7 * 2) 
    It seems like it cannot access the file calculator/pkg/calculator.py - that must be reason it's not able to fix the error.


5. The agent is not able access the calculator/pkg/calculator.py file ? That's what needs fixing.
    ~/De/w/code/courses/boot-dot-dev/build-an-ai-agent  on   main !4  uv run main.py "give me the contents of the file calculator/pkg/calculator.py"
 - Calling function: get_file_content
Traceback (most recent call last):
  File "/Users/msanjayachar/Desktop/workspace/code/courses/boot-dot-dev/build-an-ai-agent/main.py", line 102, in <module>
    main()
    ~~~~^^
  File "/Users/msanjayachar/Desktop/workspace/code/courses/boot-dot-dev/build-an-ai-agent/main.py", line 38, in main
    generate_content(client, messages, verbose)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/msanjayachar/Desktop/workspace/code/courses/boot-dot-dev/build-an-ai-agent/main.py", line 75, in generate_content
    function_call_result = call_function(function_call_part, verbose)
  File "/Users/msanjayachar/Desktop/workspace/code/courses/boot-dot-dev/build-an-ai-agent/functions/call_function.py", line 35, in call_function
    function_result = function_map[function_name](**args)
TypeError: get_file_content() got an unexpected keyword argument 'directory'

    ~/De/w/c/cou/b/build-an-ai-agent  on   main !4             
"""

"""

1. The agent is not able access the calculator/pkg/calculator.py file ? That's what needs fixing.
    ~/De/w/code/courses/boot-dot-dev/build-an-ai-agent  on   main !4  uv run main.py "give me the contents of the file calculator/pkg/calculator.py"
  1. The agent is able to access the calculator directory and is also creating a file and updating files in here. 
      But it's not able access files inside calculator/pkg. hence it's not reaching files here hence not able to get context of the bug and fix it.

  2. I am able to get the contents of a file usign `get_file_content_result = get_file_content("./", "./calculator/pkg/calculator.py")' in the main.py file
      then the agent must be calling it wrong to not get the content of the file.

3. I don't know what worked but we were able to get the contents of the file calculator/pkg/calculator.py from the agent.      

"""



