import requests
import os

def calculate_mortgage(principal, rate, years):
    monthly_rate = rate / 100 / 12
    payments = years * 12
    monthly_payment = (principal * monthly_rate) / (1 - (1 + monthly_rate)**-payments)
    return  monthly_payment

def search_product_database(query, max_results):
    database = [
        {"name": "iPhone 15", "price": 999, "currency":"USD"},
        {"name": "Samsung Galaxy S23", "price": 849, "currency":"USD"},
        {"name": "MacBook Pro", "price": 1999, "currency":"EUR"},
        {"name": "Dell XPS 13", "price": 1399, "currency":"GEL"},
    ]
    results = [item for item in database if query.lower() in item["name"].lower()]
    return results[:max_results]

def convert_currency(amount, from_currency, to_currency):
    api_key = os.getenv("EXCHANGE_API_KEY")
    # Used help from chatGPT to fix this method.
    if not api_key:
        return "API key not found."

    url = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{from_currency.upper()}/{to_currency.upper()}/{amount}"

    response = requests.get(url)

    if response.status_code != 200:
        return f"Error: Failed to fetch exchange rate. Status code: {response.status_code}"

    try:
        data = response.json()
    except Exception as e:
        return f"Error decoding JSON: {str(e)}"

    if data.get("result") != "success":
        return f"API error: {data.get('error-type', 'Unknown error')}"

    return f"{amount} {from_currency.upper()} = {data['conversion_result']} {to_currency.upper()}"