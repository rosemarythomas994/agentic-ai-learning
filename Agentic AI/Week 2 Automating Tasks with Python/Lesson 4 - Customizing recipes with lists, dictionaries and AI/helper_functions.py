import os
#os: Lets you interact with environment variables (like your API key).
from openai import OpenAI #openai: Official OpenAI client SDK for Python.
from dotenv import load_dotenv #dotenv: Used to load environment variables from a .env file.
import csv #csv: Imported, but not used in this code (maybe for later).


# Get the OpenAI API key from the .env file
load_dotenv('.env', override=True)
#Loads environment variables from a file named .env.
openai_api_key = os.getenv('OPENAI_API_KEY')
#Fetches the value of OPENAI_API_KEY (your secret key).  https://platform.openai.com/api-keys


# Set up the OpenAI client
client = OpenAI(api_key=openai_api_key)
#Creates a client object using the provided API key.This object is used to make requests to the OpenAI API.



# What it does:
# Accepts a string prompt.
# If input isn’t a string → raises error.
# Calls gpt-4o-mini with:
# A system message ("be terse") → sets assistant’s behavior.
# A user message → the actual prompt.
# temperature=0.0: makes output deterministic (less creative, more factual).
# Prints the model’s response wrapped between lines of underscores.

def print_llm_response(prompt):
    """This function takes as input a prompt, which must be a string enclosed in quotation marks,
    and passes it to OpenAI's GPT3.5 model. The function then prints the response of the model.
    """
    try:
        if not isinstance(prompt, str):
            raise ValueError("Input must be a string enclosed in quotes.")
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful but terse AI assistant who gets straight to the point.",
                },
                {"role": "user", "content": prompt},
            ],
            temperature=0.0,
        )
        response = completion.choices[0].message.content
        print("_"*100)
        print(response)
        print("_"*100)
        print("\n")
    except TypeError as e:
        print("Error:", str(e))


# What it does:
# Same as print_llm_response, but instead of printing, it returns the response as a string.
# Useful if you want to save the result to a variable, write to a file, etc.        
        
def get_llm_response(prompt):
    """This function takes as input a prompt, which must be a string enclosed in quotation marks,
    and passes it to OpenAI's GPT3.5 model. The function then saves the response of the model as
    a string.
    """
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful but terse AI assistant who gets straight to the point.",
            },
            {"role": "user", "content": prompt},
        ],
        temperature=0.0,
    )
    response = completion.choices[0].message.content
    return response


# What it does:
# Adds conversation memory.
# history is expected to be a list of past user/assistant exchanges, e.g.:
# Converts that into a big string history_string.
# Appends the new prompt → prompt_with_history.
# Sends it as a single "user" message to the model.
# Returns the response.

def get_chat_completion(prompt, history):
    history_string = "\n\n".join(["\n".join(turn) for turn in history])
    prompt_with_history = f"{history_string}\n\n{prompt}"
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful but terse AI assistant who gets straight to the point.",
            },
            {"role": "user", "content": prompt_with_history},
        ],
        temperature=0.0,
    )
    response = completion.choices[0].message.content
    return response

