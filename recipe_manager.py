low_fat_fried_chicken = {
    "name": "Low Fat Fried Chicken",
    "category": "Main Entrees",
    "prep_time": 15,
    "cook_time": 20,
    "servings": 2,
    "ingredients": ["chicken breast", "seasoning", "oil"],
    "difficulty": 2,
    "rating": 4.5
}

pizza = {
    "name": "Pizza",
    "category": "Main Entrees",
    "prep_time": 20,
    "cook_time": 15,
    "servings": 4,
    "ingredients": ["pizza dough", "pepperoni", "sausage", "mushrooms", "cheese"],
    "difficulty": 2,
    "rating": 4.7
}

cheeseburger = {
    "name": "Cheeseburger",
    "category": "Main Entrees",
    "prep_time": 10,
    "cook_time": 10,
    "servings": 1,
    "ingredients": ["ground beef", "cheese slice", "bun"],
    "difficulty": 1,
    "rating": 4.3
}

french_fries = {
    "name": "French Fries",
    "category": "Sides",
    "prep_time": 10,
    "cook_time": 15,
    "servings": 2,
    "ingredients": ["potatoes", "salt"],
    "difficulty": 1,
    "rating": 4.2
}

macaroni_and_cheese = {
    "name": "Macaroni and Cheese",
    "category": "Sides",
    "prep_time": 10,
    "cook_time": 12,
    "servings": 2,
    "ingredients": ["macaroni", "cheese", "milk"],
    "difficulty": 1,
    "rating": 4.6
}

mini_pizza = {
    "name": "Mini Pizza",
    "category": "Kids Menu",
    "prep_time": 10,
    "cook_time": 10,
    "servings": 1,
    "ingredients": ["pizza dough", "cheese"],
    "difficulty": 1,
    "rating": 4.8
}

water = {
    "name": "Water",
    "category": "Drinks",
    "prep_time": 0,
    "cook_time": 0,
    "servings": 1,
    "ingredients": ["water"],
    "difficulty": 1,
    "rating": 5
}

recipe_collection = {
    "Main Entrees": [low_fat_fried_chicken, pizza, cheeseburger],
    "Sides": [french_fries, macaroni_and_cheese],
    "Kids Menu": [mini_pizza],
    "Drinks": [water]
}

def create_recipe():
    name = input("Enter the recipe name: ")
    category = input("Enter the category (e.g., Main Entrees, Sides): ")
    prep_time = int(input("Enter preparation time in minutes: "))
    cook_time = int(input("Enter cooking time in minutes: "))
    servings = int(input("Enter number of servings: "))
    difficulty = int(input("Enter difficulty (1-5): "))
    rating = float(input("Enter rating (1-5): "))
    
    ingredients = []
    print("Enter ingredients (name). Type 'done' to stop.")
    while True:
        ingredient = input("Ingredient (name): ")
        if ingredient.lower() == 'done':
            break
        ingredients.append(ingredient)
    
    recipe = {
        "name": name,
        "category": category,
        "prep_time": prep_time,
        "cook_time": cook_time,
        "servings": servings,
        "ingredients": ingredients,
        "difficulty": difficulty,
        "rating": rating
    }
    
    return recipe

def add_recipe(collection, recipe):
    if recipe["category"] not in collection:
        print(f"Category '{recipe['category']}' doesn't exist. Adding new category.")
        collection[recipe["category"]] = []
    collection[recipe["category"]].append(recipe)

def display_recipe(recipe):
    print(f"Recipe: {recipe['name']}")
    print(f"Category: {recipe['category']}")
    print(f"Prep Time: {recipe['prep_time']} minutes | Cook Time: {recipe['cook_time']} minutes")
    print(f"Servings: {recipe['servings']}")
    print(f"Difficulty: {recipe['difficulty']} / 5 | Rating: {recipe['rating']} / 5")
    print("Ingredients:")
    for ingredient in recipe["ingredients"]:
        print(f"- {ingredient}")

def display_all_recipes(collection):
    for category, recipes in collection.items():
        print(f"\n-- {category} --")
        for r in recipes:
            print(f"{r['name']} ({r['servings']} servings)")

def search_by_name(collection, name):
    for category, recipes in collection.items():
        for r in recipes:
            if r["name"].lower() == name.lower():
                return r
    return None

# Function to search recipes by category
def search_by_category(collection, category):
    if category in collection:
        return collection[category]
    return []

def delete_recipe(collection, name):
    for category, recipes in collection.items():
        for r in recipes:
            if r["name"].lower() == name.lower():
                recipes.remove(r)
                print(f"Recipe '{name}' has been deleted.")
                return
    print(f"Recipe '{name}' not found.")

def print_menu():
    while True:
        print("\n===== RECIPE DATABASE MANAGER =====")
        print("1. Add a new recipe")
        print("2. View all recipes")
        print("3. Search recipe by name")
        print("4. Search recipes by category")
        print("5. Delete a recipe")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            recipe = create_recipe()
            add_recipe(recipe_collection, recipe)
            print(f"Recipe '{recipe['name']}' added successfully!")
        
        elif choice == "2":
            display_all_recipes(recipe_collection)
        
        elif choice == "3":
            name = input("Enter the name of the recipe: ")
            recipe = search_by_name(recipe_collection, name)
            if recipe:
                display_recipe(recipe)
            else:
                print(f"Recipe '{name}' not found.")
        
        elif choice == "4":
            category = input("Enter the category: ")
            recipes = search_by_category(recipe_collection, category)
            if recipes:
                for r in recipes:
                    print(f"{r['name']} ({r['servings']} servings)")
            else:
                print(f"No recipes found in category '{category}'.")
        
        elif choice == "5":
            name = input("Enter the name of the recipe to delete: ")
            delete_recipe(recipe_collection, name)
        
        elif choice == "6":
            print("Exiting program.")
            break
        
        else:
            print("Invalid choice, please try again.")

print_menu()
