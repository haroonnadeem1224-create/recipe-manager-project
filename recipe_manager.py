def print_menu(collection):
    for category, recipes in collection.items():
        print(f"\n-- {category} --")
        for r in recipes:
            print(f"{r['name']} ({r['servings']} servings)")

low_fat_fried_chicken = {
    "name": "Low Fat Fried Chicken",
    "category": "Main Entrees",
    "prep_time": 15,
    "cook_time": 20,
    "servings": 2,
    "ingredients": [("chicken breast", 2, "pieces"), ("seasoning", 1, "tbsp"), ("oil", 1, "cup")],
    "difficulty": 2,
    "rating": 4.5
}

pizza = {
    "name": "Pizza",
    "category": "Main Entrees",
    "prep_time": 20,
    "cook_time": 15,
    "servings": 4,
    "ingredients": [("pizza dough", 1, "unit"), ("pepperoni", 0.5, "cup"), ("sausage", 0.5, "cup"), ("mushrooms", 0.5, "cup"), ("cheese", 1, "cup")],
    "difficulty": 2,
    "rating": 4.7
}

cheeseburger = {
    "name": "Cheeseburger",
    "category": "Main Entrees",
    "prep_time": 10,
    "cook_time": 10,
    "servings": 1,
    "ingredients": [("ground beef", 1, "patty"), ("cheese slice", 1, "unit"), ("bun", 1, "unit")],
    "difficulty": 1,
    "rating": 4.3
}

french_fries = {
    "name": "French Fries",
    "category": "Sides",
    "prep_time": 10,
    "cook_time": 15,
    "servings": 2,
    "ingredients": [("potatoes", 2, "units"), ("salt", 1, "tsp")],
    "difficulty": 1,
    "rating": 4.2
}

macaroni_and_cheese = {
    "name": "Macaroni and Cheese",
    "category": "Sides",
    "prep_time": 10,
    "cook_time": 12,
    "servings": 2,
    "ingredients": [("macaroni", 1, "cup"), ("cheese", 1, "cup"), ("milk", 0.5, "cup")],
    "difficulty": 1,
    "rating": 4.6
}

mini_pizza = {
    "name": "Mini Pizza",
    "category": "Kids Menu",
    "prep_time": 10,
    "cook_time": 10,
    "servings": 1,
    "ingredients": [("pizza dough", 0.5, "unit"), ("cheese", 0.5, "cup")],
    "difficulty": 1,
    "rating": 4.8
}

water = {
    "name": "Water",
    "category": "Drinks",
    "prep_time": 0,
    "cook_time": 0,
    "servings": 1,
    "ingredients": [("water", 1, "cup")],
    "difficulty": 1,
    "rating": 5
}

recipe_collection = {
    "Main Entrees": [low_fat_fried_chicken, pizza, cheeseburger],
    "Sides": [french_fries, macaroni_and_cheese],
    "Kids Menu": [mini_pizza],
    "Drinks": [water]
}


print_menu(recipe_collection)

