import json
from datetime import datetime
from pathlib import Path


# Create folder for saved results
OUTPUT_FOLDER = Path("outputs")
OUTPUT_FOLDER.mkdir(exist_ok=True)


# Display the AI results
def display_results(analysis, action_plan):

    print("\n" + "=" * 50)
    print("STAGE 1 - SALES ANALYSIS")
    print("=" * 50)

    print(json.dumps(
        analysis,
        indent=4,
        ensure_ascii=False
    ))

    print("\n" + "=" * 50)
    print("STAGE 2 - OPTIMIZATION ACTION PLAN")
    print("=" * 50)

    print(json.dumps(
        action_plan,
        indent=4,
        ensure_ascii=False
    ))


# Save the results to a JSON file
def save_results(sales_data, analysis, action_plan):

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    output_file = OUTPUT_FOLDER / (
        f"sales_optimizer_{timestamp}.json"
    )

    results = {
        "generated_at": datetime.now().isoformat(),
        "sales_data": sales_data,
        "stage_1_analysis": analysis,
        "stage_2_action_plan": action_plan
    }

    try:
        with open(
            output_file,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                results,
                file,
                indent=4,
                ensure_ascii=False
            )

        print("\nResults saved successfully.")
        print(f"File: {output_file}")

    except OSError as error:
        print(f"Could not save results: {error}")