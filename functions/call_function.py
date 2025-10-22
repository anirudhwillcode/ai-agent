from functions.get_files_info import get_files_info
from functions.get_file_contents import get_file_contents
from functions.write_file import write_file
from functions.run_python_file import run_python_file
from google.genai import types

working_directory = "calculator"

def call_function(function_call_part, verbose=False):
    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")

    # Use dictionary dispatch for cleaner mapping
    function_map = {
        "get_files_info": get_files_info,
        "get_file_content": get_file_contents,  # ✅ fixed: should match schema name
        "write_file": write_file,
        "run_python_file": run_python_file,
    }

    func = function_map.get(function_call_part.name)
    if not func:
        # Unknown function — return error response
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_call_part.name,
                    response={"error": f"Unknown function: {function_call_part.name}"},
                )
            ],
        )

    # Execute safely
    try:
        result = func(working_directory, **function_call_part.args)
    except Exception as e:
        result = {"error": str(e)}

    # Build the response object
    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_call_part.name,
                response={"result": result},
            )
        ],
    )
