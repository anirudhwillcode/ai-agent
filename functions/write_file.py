import os
from google.genai import types
def write_file(working_directory , file_path , content):
    abs_working_dir=os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory,file_path))    
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    # If file path does not exist create it

    parent_dir = os.path.dirname(abs_file_path)


    if not os.path.exists(parent_dir):
        os.makedirs(parent_dir , mode = 0o777, exist_ok=True)

    
    with open(abs_file_path, "w") as f:
        f.write(content)
        print(f'Successfully wrote to "{file_path}" ({len(content)} characters written)')
    
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="safely writes text to a file within a permitted working directory: it verifies the path is allowed, creates missing folders, overwrites the file with the given content, and returns a success or error message.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The target file’s path to write to.",
            ),
            "content":types.Schema(
                type=types.Type.STRING,
                description="The content to write to the file as a string"
            ),
        },
    ),
)

