from openai import OpenAI
import os
import json
from Helpers import calculate_mortgage, search_product_database, convert_currency
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

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
        "name": "convert_currency",
        "description": "Convert money from one currency to another.",
        "parameters": {
            "type": "object",
            "properties": {
                "amount": {"type": "number"},
                "from_currency": {"type": "string"},
                "to_currency": {"type": "string"}
            },
            "required": ["amount", "from_currency", "to_currency"]
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

        response = client.chat.completions.create(
            model=os.getenv("OPEN_AI_MODEL"),
            messages=messages,
            functions=function_definitions,
            function_call="auto"
        )

        message = response.choices[0].message

        if message.function_call:
            function_name = message.function_call.name
            arguments = json.loads(message.function_call.arguments)

            if function_name == "calculate_mortgage":
                result = calculate_mortgage(**arguments)
            elif function_name == "search_product_database":
                result = search_product_database(**arguments)
            elif function_name == "convert_currency":
                result = convert_currency(**arguments)
            else:
                result = "Unknown function."

            print(f"Assistant: {function_name} result: {result}")

            messages.append({
                "role": "function",
                "name": function_name,
                "content": json.dumps(result)
            })
        else:
            print(f"Assistant: {message.content}")

if __name__ == "__main__":
    run_chat()

# TEST QUESTIONS

# 1. How much does an Iphone cost?
# 2. What would be my monthly rate on that Iphone, if I bought with 10% interest for a 5 year period?
# 3. How about for a 3 year period, with 5% interest?
# 4. Convert that amount to Georgian Lari.
# 5. Now convert that amount to Euro.