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


def get_files_info(working_directory, directory="."):
    # it is given that the abs path to the dicectory is outside the working directory return error msg
    # it means that
    
    abs_working_dir = os.path.abspath(
        working_directory
    )  # /home/anirudh/projects/calculator

    abs_directory = ""
    if directory is None:
        abs_directory = os.path.abspath(
            working_directory
        )  # /home/anirudh/projects/calculator
    else:
        abs_directory = os.path.abspath(os.path.join(working_directory, directory))

    if not abs_directory.startswith(abs_working_dir):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    # return a string representing the contents of the directory
    full_content = ""
    contents = os.listdir(abs_directory)
    for content in contents:
        file_size = os.path.getsize(os.path.join(abs_directory, content))
        is_directory = os.path.isdir(os.path.join(abs_directory, content))
        full_content += (
            f"{content}: file_size = {file_size} bytes, is_dir={is_directory}\n"
        )

    return full_content

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

