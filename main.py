import openai
import os
import json
from Helpers import  calculate_mortgage, search_product_database

openai.api_key = os.getenv("OPEN_API_KEY")

function_definitions = [
    {
        "name": "calculate_mortgage",
        "description": "Calculate monthly mortgage payment.",
        "parameters": {
            "type": "object",
            "properties": {
                "principal": {"type": "number"},
                "rate": {"type": "number"},
                "years": {"type": "number"}
            },
            "required": ["principal", "rate", "years"]
        }
    },
    {
        "name": "search_product_database",
        "description": "Search for products by name.",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {"type": "string"},
                "max_results": {"type": "integer"}
            },
            "required": ["query", "max_results"]
        }
    }
]

def run_chat():
    print("Type 'exit' to quit.\n")
    messages = [{"role": "system", "content": "You are a helpful assistant."}]

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break

        messages.append({"role": "user", "content": user_input})

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0613",
            messages=messages,
            functions=function_definitions,
            function_call="auto"
        )

        message = response["choices"][0]["message"]

        if message.get("function_call"):
            function_name = message["function_call"]["name"]
            arguments = json.loads(message["function_call"]["arguments"])

            if function_name == "calculate_mortgage":
                result = calculate_mortgage(**arguments)
            elif function_name == "search_product_database":
                result = search_product_database(**arguments)
            else:
                result = "Unknown function."

            print(f"Assistant: {function_name} result: {result}")

            messages.append({
                "role": "function",
                "name": function_name,
                "content": json.dumps(result)
            })
        else:
            print(f"Assistant: {message['content']}")

if __name__ == "__main__":
    run_chat()