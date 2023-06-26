#file for testing if i am able to create a function which always generates hello world
import openai
openai.api_key = "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"
import json


def say_hello_world():
    """Always return 'Hello, World!'"""
    return "Hello, World!"

def run_conversation():
    # Step 1: send the conversation and available functions to GPT
    messages = [{"role": "user", "content": "Say hello to the world for me!"}]
    functions = [
        {
            "name": "say_hello_world",
            "description": "Always return 'Hello, World!'",
            "parameters": {}
        }
    ]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",  # or "gpt-4-0613"
        messages=messages,
        functions=functions,
        function_call="auto",  # auto is default, but we'll be explicit
    )
    response_message = response["choices"][0]["message"]

    # Step 2: check if GPT wanted to call a function
    if response_message.get("function_call"):
        # Step 3: call the function
        available_functions = {
            "say_hello_world": say_hello_world,
        }
        function_name = response_message["function_call"]["name"]
        function_to_call = available_functions[function_name]
        function_response = function_to_call()

        # Step 4: send the info on the function call and function response to GPT
        messages.append(response_message)  # extend conversation with assistant's reply
        messages.append(
            {
                "role": "function",
                "name": function_name,
                "content": function_response,
            }
        )  # extend conversation with function response
        second_response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0613",  # or "gpt-4-0613"
            messages=messages,
        )  # get a new response from GPT where it can see the function response
        return second_response


print(run_conversation())
