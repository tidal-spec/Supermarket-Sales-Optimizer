import os
import time
from dotenv import load_dotenv
from google import genai
from google.genai.errors import APIError


load_dotenv(); api_key = os.getenv("GEMINI_API_KEY")
if not api_key: raise ValueError("❌ GEMINI_API_KEY not found in environment.")
client = genai.Client(api_key=api_key); MOD_POOL = ["gemini-2.0-flash", "gemini-1.5-flash", "gemini-1.5-pro"]

def safe_generate_content(prompt):
    for model in MOD_POOL:
        try: return client.models.generate_content(model=model, contents=prompt).text.strip()
        except APIError: time.sleep(2)
    raise Exception("❌ All model candidates failed.")

def main():
    rag_catalog = read_rag()
    while True:
        choice = input("\n1. Analyze Issue | 2. Exit\nSelect option: ").strip()
        if choice == "2": break
        if choice == "1":
            inp = input("Describe store inventory issue:\n> "); json_res = stage_1(inp, safe_generate_content)
            if "Irrelevant_Input" in json_res:
                print("👋 Guardrail Triggered: Ask questions related to supermarket stock!"); continue
            plan = stage_2(json_res, rag_catalog, safe_generate_content); print(f"\n{plan}\n"); save_action_plan(plan)

if __name__ == "__main__": main()
