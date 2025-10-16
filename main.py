import os
from dotenv import load_dotenv
from google import genai
import sys
from google.genai import types

load_dotenv()
api_key=os.environ.get("GEMINI_API_KEY")
client =  genai.Client(api_key=api_key)

def main():

    # When you run your python script like this python myscript.py " Who is Chris"
    # Python puts everything you type into a list called sys.argv 
    # the list looks like this : ["myscript.py", "Who", "world"]
   

    args = sys.argv[1:]

    if not args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here"')
        sys.exit(1)
    user_prompt=" ".join(args)

    messages = [
        types.Content(role="user",parts =[types.Part(text=user_prompt)])
    ]

    response = client.models.generate_content(
        model='gemini-2.0-flash-001',
        contents= messages,
     )
    
    if "--verbose" in user_prompt:

        
        print("---------------------------------------------")
        print(response.text)
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    else:
        print(response.text)
    

if __name__ == "__main__":
    main()
