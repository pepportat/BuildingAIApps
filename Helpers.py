def calculate_mortgage(principal, rate, years):
    monthly_rate = rate / 100 / 12
    payments = years * 12
    monthly_payment = (principal * monthly_rate) / (1 - (1 + monthly_rate)**-payments)
    return  monthly_payment

def search_product_database(query, max_results):
    database = [
        {"name": "iPhone 15", "price": 999},
        {"name": "Samsung Galaxy S23", "price": 849},
        {"name": "MacBook Pro", "price": 1999},
        {"name": "Dell XPS 13", "price": 1399},
    ]
    results = [item for item in database if query.lower() in item["name"].lower()]
    return results[:max_results]
