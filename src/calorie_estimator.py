# Mock calorie table for example
calorie_table = {
    "fried_rice": {
        "boiled": 250,
        "fried": 450
    },
    "sushi": {
        "raw": 200,
        "fried": 350
    }
}

def estimate_calorie(food_type, cook_method="default", quantity=1):
    base = calorie_table.get(food_type, {}).get(cook_method, 0)
    return base * quantity

