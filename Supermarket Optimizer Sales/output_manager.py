import json
from datetime import datetime
from pathlib import Path

# Create folder for saved results
OUTPUT_FOLDER = Path("outputs")
OUTPUT_FOLDER.mkdir(exist_ok=True)


# Display the AI results
def display_results(analysis, action_plan):
    """Prints the sales analysis and optimization action plan formatted as JSON."""
    print("\n" + "=" * 50)
    print("STAGE 1 - SALES ANALYSIS")
    print("=" * 50)

    print(json.dumps(analysis, indent=4, ensure_ascii=False))

    print("\n" + "=" * 50)
    print("STAGE 2 - OPTIMIZATION ACTION PLAN")
    print("=" * 50)

    print(json.dumps(action_plan, indent=4, ensure_ascii=False))


# Save the results to a JSON file
def save_results(sales_data, analysis, action_plan):
    """Saves the input data, analysis, and action plan to a timestamped JSON file."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = OUTPUT_FOLDER / f"sales_optimizer_{timestamp}.json"

    results = {
        "generated_at": datetime.now().isoformat(),
        "sales_data": sales_data,
        "stage_1_analysis": analysis,
        "stage_2_action_plan": action_plan,
    }

    try:
        with open(output_file, "w", encoding="utf-8") as file:
            json.dump(results, file, indent=4, ensure_ascii=False)

        print("\nResults saved successfully.")
        print(f"File: {output_file}")

    except OSError as error:
        print(f"Could not save results: {error}")


if __name__ == "__main__":
    # Example test payload to run the script standalone
    sample_sales_data = {"item": "Milk", "quantity_sold": 150, "revenue": 450.0}
    sample_analysis = {"status": "High Demand", "stock_level": "Low"}
    sample_action_plan = {"recommendation": "Restock 200 units by Friday."}

    display_results(sample_analysis, sample_action_plan)
    save_results(sample_sales_data, sample_analysis, sample_action_plan)