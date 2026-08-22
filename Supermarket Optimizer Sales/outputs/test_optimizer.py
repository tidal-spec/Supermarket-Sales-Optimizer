from output_manager import save_results


# Test that results can be saved
def test_save_results():

    sales_data = [
        {
            "name": "Test Product",
            "category": "Food",
            "units_sold": 20,
            "current_stock": 5,
            "selling_price_kes": 100,
            "cost_price_kes": 60
        }
    ]

    analysis = {
        "best_selling_products": ["Test Product"],
        "slow_moving_products": [],
        "low_stock_products": ["Test Product"],
        "overstock_products": [],
        "key_observations": [
            "Test product has low stock."
        ]
    }

    action_plan = {
        "priority_actions": [
            "Review stock level."
        ],
        "restocking_recommendations": [
            "Consider replenishment."
        ],
        "promotion_ideas": [],
        "inventory_actions": [],
        "waste_reduction_actions": [],
        "seven_day_action_plan": [
            "Review product sales."
        ]
    }

    save_results(
        sales_data,
        analysis,
        action_plan
    )

    print("Test completed successfully.")


if __name__ == "__main__":
    test_save_results()