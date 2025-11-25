recipes = {
    "Breakfast meat sandwich with egg and cheese": {
        "category": "breakfast",
        "ingredients": ["bread", "egg", "cheese", "breakfast meat"],
        "prep_time": 10,
        "cook_time": 5,
        "difficulty": "easy"
    },
    "Veggie omelette": {
        "category": "breakfast",
        "ingredients": ["eggs", "spinach", "bell pepper", "onion"],
        "prep_time": 5,
        "cook_time": 7,
        "difficulty": "easy"
    },
    "Double bacon cheeseburger (two patties)": {
        "category": "lunch",
        "ingredients": ["beef patties", "bacon", "cheese", "bun"],
        "prep_time": 10,
        "cook_time": 12,
        "difficulty": "medium"
    },
    "Salad": {
        "category": "lunch",
        "ingredients": ["lettuce", "tomato", "cucumber", "dressing"],
        "prep_time": 5,
        "cook_time": 0,
        "difficulty": "easy"
    },
    "Steak with compound butter": {
        "category": "dinner",
        "ingredients": ["steak", "butter", "herbs"],
        "prep_time": 10,
        "cook_time": 12,
        "difficulty": "medium"
    },
    "Chicken and brown rice": {
        "category": "dinner",
        "ingredients": ["chicken", "brown rice", "seasoning"],
        "prep_time": 5,
        "cook_time": 25,
        "difficulty": "easy"
    }
}

meal_plan = {
    "Monday": {"breakfast": {}, "lunch": {}, "dinner": {}}
}

recipe_usage = {}

def add_meal(day, meal_type, recipe_name, quantity=1):
    if day not in meal_plan:
        meal_plan[day] = {"breakfast": {}, "lunch": {}, "dinner": {}}
    meal_plan[day][meal_type][recipe_name] = meal_plan[day][meal_type].get(recipe_name, 0) + quantity
    recipe_usage[recipe_name] = recipe_usage.get(recipe_name, 0) + quantity

def display_weekly_plan():
    print("\n==============================")
    print("        WEEKLY MEAL PLAN")
    print("==============================\n")

    for day, meals in meal_plan.items():
        print(day)
        print("--------------------------------")
        for meal_type, items in meals.items():
            print(f"{meal_type.title()}:")
            if items:
                for recipe, qty in items.items():
                    print(f"  • {recipe} (x{qty})")
            else:
                print("  • None")
            print()

def display_recipe_usage():
    print("==============================")
    print("         RECIPE USAGE")
    print("==============================\n")
    for recipe, qty in recipe_usage.items():
        print(f"{recipe:<45} : {qty}")

def most_used_recipes():
    if not recipe_usage:
        return []
    max_qty = max(recipe_usage.values())
    return [r for r, q in recipe_usage.items() if q == max_qty]


monday_meals = {
    "breakfast": [
        ("Breakfast meat sandwich with egg and cheese", 1),
        ("Veggie omelette", 2)
    ],
    "lunch": [
        ("Double bacon cheeseburger (two patties)", 4),
        ("Salad", 3)
    ],
    "dinner": [
        ("Steak with compound butter", 1),
        ("Chicken and brown rice", 2)
    ]
}

for meal_type, recipe_list in monday_meals.items():
    for recipe, qty in recipe_list:
        add_meal("Monday", meal_type, recipe, qty)

display_weekly_plan()
display_recipe_usage()

print("\nMost used recipes:")
for r in most_used_recipes():
    print(f"  • {r}")

