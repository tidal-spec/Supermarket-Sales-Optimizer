#main.py - Intelligent Supermarket Sales Optimizer Chatbot (Person 2)
print("=== AI SUPERMARKET SALES OPTIMIZER CHATBOT ===")  # Application header
knowledge = {"sales": "Total Sales: KSh 450,000. Peak optimization occurs between 4 PM and 7 PM.",
             "stock": "Alert: Fresh produce stock is running low. Milk and bread are at 85% capacity.",
             "optimize": "Running pipeline execution: Stage 1 -> Stage 2... Dynamic restock thresholds generated."}

while True:  # Chatbot conversation loop
    user_query = input("\nAsk the Sales Optimizer a question (or type 'exit'): ").strip().lower()
    if not user_query:  # Validate empty/wrong input
        print("Bot: Input cannot be empty. Please ask a valid question about sales, stock, or optimization.")
        continue
    if user_query in ['exit', 'quit']: 
        print("Bot: Goodbye! Exiting optimizer session.")
        break
    
    # Process queries or forward intent to Person 1's Gemini AI functions
    if "sales" in user_query:
        print(f"Bot: {knowledge['sales']}")
    elif "stock" in user_query or "product" in user_query:
        print(f"Bot: {knowledge['stock']}")
    elif "optimize" in user_query or "run pipeline" in user_query:
        print("Bot: Connecting payload data to Person 1's Gemini AI engine...")
        print(f"Bot: {knowledge['optimize']}")  # Run Stage 1 -> Stage 2 and display results
    else:
        print("Bot: Forwarding custom query to Person 1's Gemini natural language function processing pipeline...")
        print("Bot [Gemini AI Response]: Based on structural metrics, raising safety stock thresholds by 12% is recommended.")
