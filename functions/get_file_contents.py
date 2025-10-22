import os
from google.genai import types
# os.path.abspath(): Get an absolute path from a relative path
# os.path.join(): Join two paths together safely (handles slashes)
# .startswith(): Check if a string starts with a substring
# os.path.isdir(): Check if a path is a directory
# os.listdir(): List the contents of a directory
# os.path.getsize(): Get the size of a file
# os.path.isfile(): Check if a path is a file
# .join(): Join a list of strings together with a separator

# ---------------------------------------------------------------------------------------------------

# os.path.abspath: Get an absolute path from a relative path
# os.path.join: Join two paths together safely (handles slashes)
# .startswith: Check if a string starts with a specific substring
# os.path.isfile: Check if a path is a file

MAX_CHARS = 10000
def get_file_contents(working_directory,file_path):
    abs_working_dir=os.path.abspath(working_directory)
    actual_file_path = os.path.abspath(os.path.join(working_directory,file_path))    
    if not actual_file_path.startswith(abs_working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(actual_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    file_content_string = ""
    try:
        with open(actual_file_path,"r") as f:
            file_content_string = f.read(MAX_CHARS)
            if len(file_content_string) >= MAX_CHARS:
                file_content_string += f'[...File "{file_path}" truncated at 10000 characters]'   
        return file_content_string
    except Exception as e:
        return f"Exception reading file: {e}"

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Read the file content and print it ",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path of a file to get the contents ",
            ),
        },
    ),
)



    

    


