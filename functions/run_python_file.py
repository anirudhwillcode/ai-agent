import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path: str, args=[]):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory,file_path))
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(abs_file_path):
        return f'File "{file_path}" not found.'
    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.' 
    
    try:
        final_args = ["python3", file_path]
        final_args.extend(args)
        result = subprocess.run(
            final_args,
            cwd=abs_working_dir,
            timeout=30,
            capture_output=True
        )
        final_string = f"""
STDOUT: {result.stdout}
STDERR: {result.stderr}
"""
        
        if result.stdout == "" and result.stderr == "":
            final_string = "No output produced.\n"
        if result.returncode !=0:
            final_string = f"Process exited with code {result.returncode}"
        return final_string
    except Exception as e:
        return f"Error: executing Python file: {e}"

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="It’s a helper function that safely executes a Python file inside a specified working directory and returns a formatted summary of the run",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path of a file to get the contents ",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(type=types.Type.STRING),
                description="Optional list of extra command-line arguments passed to the Python file. ",
            ),
        },
    ),
)