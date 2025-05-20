# LLM Function Calling Chat Assistant

This is a simple Python-based chat assistant powered by OpenAI's GPT and function calling capabilities. It supports three built-in functions:

1. **Mortgage Calculator**
2. **Product Database Search**
3. **Currency Conversion** (using [Exchangerate-API](https://www.exchangerate-api.com/) – API key required)

## Features

- Conversational CLI interface
- Automatic function calling using OpenAI's latest API
- Real-time currency conversion without API key
- Clean modular code using `Helpers.py`

---

## Example Queries

Here are five example queries to demonstrate function calling:

1. **"How much does an Iphone cost?"**  
   → Calls `search_product_database`

2. **"What would be my monthly rate on that Iphone, if I bought with 10% interest for a 5 year period?"**  
   → Calls `calculate_mortgage`

3. **"How about for a 3 year period, with 5% interest?"**  
   → Calls `calculate_mortgage`

4. **"Convert that amount to Georgian Lari."**  
   → Calls `currency_converter`

5. **"Now convert that amount to Euro."**  
   → Calls `currency_converter`

---

##  Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/llm-function-calling-chat.git
cd llm-function-calling-chat
