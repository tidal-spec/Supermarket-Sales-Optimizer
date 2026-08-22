import os, json, dotenv, google.genai as genai, google.genai.types as types

dotenv.load_dotenv(dotenv.find_dotenv(usecwd=True), override=True)
api_key = os.getenv("GEMINI_API_KEY") or "PASTE_YOUR_WORKING_API_KEY_HERE"
client = genai.Client(api_key=api_key)

# Dynamically fetch ALL active models supporting content generation
def get_all_models():
    try:
        return [m.name for m in client.models.list() if "generateContent" in getattr(m, "supported_actions", []) or "generateContent" in getattr(m, "supported_generation_methods", [])]
    except Exception:
        return ["gemini-2.5-flash", "gemini-1.5-flash"]

def call_ai(prompt):
    cfg = types.GenerateContentConfig(response_mime_type="application/json")
    for m in get_all_models():
        try:
            return json.loads(client.models.generate_content(model=m, contents=prompt, config=cfg).text)
        except Exception:
            continue
    raise RuntimeError("All dynamic AI model attempts failed.")

def analyze_sales(data):
    return call_ai(f"ROLE: Analyst. TASK: Find top/slow/low/overstocked items in Kenya store. CONSTRAINTS: Given data only, JSON output. DATA: {json.dumps(data)}")

def create_action_plan(data, analysis):
    return call_ai(f"ROLE: Advisor. TASK: 7-day plan for Kenya store. CONSTRAINTS: Realistic actions, JSON output. DATA: {json.dumps(data)} ANALYSIS: {json.dumps(analysis)}")

if __name__ == "__main__":
    print("Testing dynamic multi-model AI pipeline...")
    sample = {"items": [{"name": "Unga 2kg", "stock": 2, "sales": 50}]}
    res1 = analyze_sales(sample)
    print("\n--- STAGE 2 ACTION PLAN OUTPUT ---")
    print(json.dumps(create_action_plan(sample, res1), indent=2))