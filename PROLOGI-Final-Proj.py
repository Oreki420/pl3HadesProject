import random
import csv
import os
import tkinter as tk
from tkinter import ttk

# Define the dietary restrictions
diets = ["none", "vegetarian", "vegan", "pescatarian", "gluten-free", "dairy-free"]

# Define the available cuisines
cuisines = ["Italian", "Mexican", "Indian", "Chinese", "Thai", "Mediterranean"]

# Define the meal options for each cuisine
italian_meals = ["Pasta", "Pizza", "Risotto", "Lasagna", "Minestrone", "Tiramisu"]
mexican_meals = ["Tacos", "Burritos", "Enchiladas", "Chiles Rellenos", "Guacamole", "Flan"]
indian_meals = ["Curry", "Biryani", "Tandoori Chicken", "Chana Masala", "Naan", "Gulab Jamun"]
chinese_meals = ["Kung Pao Chicken", "Fried Rice", "Spring Rolls", "Dumplings", "Hot and Sour Soup", "Fortune Cookies"]
thai_meals = ["Pad Thai", "Green Curry", "Tom Yum", "Pad See Ew", "Som Tum", "Mango Sticky Rice"]
mediterranean_meals = ["Falafel", "Greek Salad", "Hummus", "Shawarma", "Moussaka", "Baklava"]

# Define a dictionary for meal options
meal_options = {
    "Italian": italian_meals,
    "Mexican": mexican_meals,
    "Indian": indian_meals,
    "Chinese": chinese_meals,
    "Thai": thai_meals,
    "Mediterranean": mediterranean_meals
}

# Add the dictionary for meal nutritional information here

meal_nutrition = {
    "Pasta": {"calories": 400, "protein": 14, "fat": 12, "carbs": 60},
    "Pizza": {"calories": 300, "protein": 12, "fat": 10, "carbs": 40},
    "Risotto": {"calories": 480, "protein": 12, "fat": 15, "carbs": 75},
    "Lasagna": {"calories": 350, "protein": 18, "fat": 15, "carbs": 35},
    "Minestrone": {"calories": 190, "protein": 6, "fat": 2, "carbs": 35},
    "Tiramisu": {"calories": 450, "protein": 8, "fat": 18, "carbs": 60},
    "Tacos": {"calories": 250, "protein": 12, "fat": 10, "carbs": 25},
    "Burritos": {"calories": 500, "protein": 20, "fat": 15, "carbs": 65},
    "Enchiladas": {"calories": 350, "protein": 20, "fat": 15, "carbs": 40},
    "Chiles Rellenos": {"calories": 290, "protein": 12, "fat": 18, "carbs": 20},
    "Guacamole": {"calories": 230, "protein": 3, "fat": 20, "carbs": 12},
    "Flan": {"calories": 300, "protein": 6, "fat": 11, "carbs": 45},
    "Curry": {"calories": 550, "protein": 28, "fat": 25, "carbs": 50},
    "Biryani": {"calories": 600, "protein": 25, "fat": 15, "carbs": 80},
    "Tandoori Chicken": {"calories": 300, "protein": 40, "fat": 5, "carbs": 10},
    "Chana Masala": {"calories": 350, "protein": 15, "fat": 5, "carbs": 60},
    "Naan": {"calories": 250, "protein": 7, "fat": 8, "carbs": 40},
    "Gulab Jamun": {"calories": 150, "protein": 2, "fat": 5, "carbs": 25},
    "Kung Pao Chicken": {"calories": 400, "protein": 30, "fat": 18, "carbs": 35},
    "Fried Rice": {"calories": 550, "protein": 12, "fat": 20, "carbs": 80},
    "Spring Rolls": {"calories": 100, "protein": 2, "fat": 5, "carbs": 10},
    "Dumplings": {"calories": 250, "protein": 8, "fat": 10, "carbs": 30},
 "Hot and Sour Soup": {"calories": 90, "protein": 4, "fat": 1, "carbs": 13},
    "Fortune Cookies": {"calories": 30, "protein": 0, "fat": 0, "carbs": 7},
    "Pad Thai": {"calories": 600, "protein": 25, "fat": 20, "carbs": 75},
    "Green Curry": {"calories": 450, "protein": 30, "fat": 20, "carbs": 20},
    "Tom Yum": {"calories": 200, "protein": 15, "fat": 5, "carbs": 20},
    "Pad See Ew": {"calories": 550, "protein": 25, "fat": 15, "carbs": 75},
    "Som Tum": {"calories": 150, "protein": 3, "fat": 0, "carbs": 35},
    "Mango Sticky Rice": {"calories": 500, "protein": 6, "fat": 15, "carbs": 90},
    "Falafel": {"calories": 350, "protein": 13, "fat": 18, "carbs": 30},
    "Greek Salad": {"calories": 200, "protein": 6, "fat": 15, "carbs": 10},
    "Hummus": {"calories": 160, "protein": 7, "fat": 9, "carbs": 15},
    "Shawarma": {"calories": 550, "protein": 35, "fat": 20, "carbs": 50},
    "Moussaka": {"calories": 400, "protein": 20, "fat": 22, "carbs": 30},
    "Baklava": {"calories": 400, "protein": 6, "fat": 24, "carbs": 42}
}

# Define a dictionary for meal ingredients (simplified for demonstration purposes)
meal_ingredients = {
    "Pasta": ["pasta", "tomato sauce", "cheese"],
    "Pizza": ["pizza dough", "tomato sauce", "cheese", "toppings"],
    "Risotto": ["arborio rice", "vegetable broth", "white wine", "butter", "onions", "Parmesan cheese"],
    "Lasagna": ["lasagna noodles", "tomato sauce", "ground beef", "ricotta cheese", "mozzarella cheese", "Parmesan cheese"],
    "Minestrone": ["vegetable broth", "diced tomatoes", "onions", "carrots", "celery", "beans", "pasta"],
    "Tiramisu": ["ladyfingers", "espresso", "mascarpone cheese", "egg yolks", "sugar", "cocoa powder"],
    "Tacos": ["tortillas", "ground beef", "onions", "tomatoes", "lettuce", "cheese", "salsa"],
    "Burritos": ["tortillas", "rice", "beans", "ground beef", "cheese", "salsa", "sour cream"],
    "Enchiladas": ["tortillas", "enchilada sauce", "chicken", "cheese", "onions", "olives"],
    "Chiles Rellenos": ["poblano peppers", "cheese", "eggs", "flour", "tomato sauce"],
    "Guacamole": ["avocados", "tomatoes", "onions", "jalapenos", "cilantro", "lime", "garlic"],
    "Flan": ["sugar", "evaporated milk", "condensed milk", "eggs", "vanilla extract"],
    "Curry": ["rice", "chicken", "onions", "tomatoes", "coconut milk", "curry powder", "garlic", "ginger"],
    "Biryani": ["rice", "chicken", "yogurt", "onions", "tomatoes", "garlic", "ginger", "biryani spices"],
    "Tandoori Chicken": ["chicken", "yogurt", "tandoori masala", "ginger", "garlic", "lime"],
    "Chana Masala": ["chickpeas", "onions", "tomatoes", "garlic", "ginger", "garam masala", "coriander"],
    "Naan": ["flour", "yogurt", "baking powder", "sugar", "salt", "water", "butter"],
    "Gulab Jamun": ["milk powder", "flour", "baking soda", "ghee", "milk", "sugar", "water", "rose water", "cardamom"],
    "Kung Pao Chicken": ["chicken", "bell peppers", "peanuts", "soy sauce", "hoisin sauce", "cornstarch", "ginger", "garlic"],
    "Fried Rice": ["rice", "vegetable oil", "onions", "carrots", "peas", "soy sauce", "eggs"],
    "Spring Rolls": ["spring roll wrappers", "cabbage", "carrots", "mushrooms", "soy sauce", "oil"],
    "Dumplings": ["ground pork", "cabbage", "green onions", "ginger", "garlic", "soy sauce", "dumpling wrappers"],
    "Hot and Sour Soup": ["chicken broth", "soy sauce", "rice vinegar", "cornstarch", "tofu", "mushrooms", "eggs", "bamboo shoots"],
    "Fortune Cookies": ["flour", "sugar", "cornstarch", "egg whites", "vanilla extract", "almond extract", "water"],
    "Pad Thai": ["rice noodles", "shrimp", "bean sprouts", "green onions", "eggs", "tamarind paste", "fish sauce", "sugar", "lime", "peanuts"],
    "Green Curry": ["chicken", "coconut milk", "green curry paste", "eggplant", "bell peppers", "basil", "fish sauce", "sugar"],
    "Tom Yum": ["shrimp", "lemongrass", "galangal", "kaffir lime leaves", "tom yum paste", "fish sauce", "lime", "mushrooms", "coconut milk"],
    "Pad See Ew": ["rice noodles", "chicken", "Chinese broccoli", "eggs", "soy sauce", "oyster sauce", "sugar"],
    "Som Tum": ["green papaya", "tomatoes", "green beans", "garlic", "chili peppers", "lime", "fish sauce", "palm sugar", "peanuts"],
    "Mango Sticky Rice": ["sticky rice", "coconut milk", "sugar", "salt", "mango"],
    "Falafel": ["chickpeas", "onions", "parsley", "garlic", "cumin", "coriander", "flour", "oil"],
    "Greek Salad": ["cucumbers", "tomatoes", "red onions", "olives", "feta cheese", "olive oil", "lemon juice", "oregano"],
    "Hummus": ["chickpeas", "tahini", "garlic", "lemon juice", "olive oil", "cumin", "salt"],
    "Shawarma": ["chicken", "yogurt", "shawarma spices", "garlic", "lemon juice", "tahini", "pickles", "tomatoes", "lettuce"],
    "Moussaka": ["eggplant", "ground beef", "onions", "tomato sauce", "potatoes", "béchamel sauce", "Parmesan cheese"],
    "Baklava": ["phyllo dough", "walnuts", "sugar", "cinnamon", "butter", "honey", "lemon juice", "water"]
}


# Define a function to filter meals based on user preferences
def filter_meals(meals, restrictions):
    filtered_meals = []

    for meal in meals:
        ingredients = meal_ingredients[meal]
        if restrictions == "vegetarian":
            if not any(ingredient in ["ground beef", "chicken", "shrimp", "fish"] for ingredient in ingredients):
                filtered_meals.append(meal)
        elif restrictions == "vegan":
            if not any(ingredient in ["ground beef", "chicken", "shrimp", "fish", "cheese", "egg", "butter", "milk",
                                      "yogurt", "eggs"] for ingredient in ingredients):
                filtered_meals.append(meal)
        elif restrictions == "pescatarian":
            if not any(ingredient in ["ground beef", "chicken"] for ingredient in ingredients):
                filtered_meals.append(meal)
        elif restrictions == "gluten-free":
            if not any(ingredient in ["pasta", "pizza dough", "lasagna noodles", "flour", "wheat"] for ingredient in
                       ingredients):
                filtered_meals.append(meal)
        elif restrictions == "dairy-free":
            if not any(ingredient in ["cheese", "milk", "butter", "yogurt", "cream"] for ingredient in ingredients):
                filtered_meals.append(meal)
        else:
            filtered_meals.append(meal)

    return filtered_meals

# Define a function to export meal options to a CSV file
def export_to_csv():
    with open("meal_options.csv", mode="w", newline='') as csv_file:
        fieldnames = ["Meal", "Calories", "Protein", "Carbs", "Fat"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for meal, nutrition in meal_options.items():
            writer.writerow({"Meal": meal, "Calories": nutrition["Calories"],
                             "Protein": nutrition["Protein"], "Carbs": nutrition["Carbs"],
                             "Fat": nutrition["Fat"]})

# Define a function to update the list of meals and nutritional information based on the user's preferences
def update_meals():
    chosen_cuisine = cuisine_var.get()
    chosen_diet = diet_var.get()
    meals = meal_options[chosen_cuisine]
    filtered_meals = filter_meals(meals, chosen_diet)
    meal_list.delete(0, tk.END)
    for meal in filtered_meals:
        meal_list.insert(tk.END, meal)

def update_nutrition():
    chosen_meal = meal_list.get(tk.ACTIVE)
    nutrition = meal_nutrition[chosen_meal]
    nutrition_label.config(text=f"Calories: {nutrition['calories']} | Protein: {nutrition['protein']}g | Fat: {nutrition['fat']}g | Carbs: {nutrition['carbs']}g")

def export_grocery_list():
    filename = "grocery_list.csv"
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Grocery List'])
        for item in grocery_list:
            writer.writerow([item])
    print(f"\nGrocery list exported as {filename}")

# Create the main application window
root = tk.Tk()
root.title("Meal Suggestion App")

# Create frames for the input widgets and the listbox
input_frame = ttk.Frame(root, padding="10 10 10 10")
input_frame.grid(row=0, column=0, sticky=tk.W+tk.E)
list_frame = ttk.Frame(root, padding="10 0 10 10")
list_frame.grid(row=1, column=0, sticky=tk.W+tk.E)

# Create the input widgets
cuisine_label = ttk.Label(input_frame, text="Cuisine:")
cuisine_label.grid(row=0, column=0, sticky=tk.W)
cuisine_var = tk.StringVar()
cuisine_menu = ttk.OptionMenu(input_frame, cuisine_var, *cuisines)
cuisine_menu.grid(row=0, column=1, sticky=tk.W)

diet_label = ttk.Label(input_frame, text="Dietary Restrictions:")
diet_label.grid(row=1, column=0, sticky=tk.W)
diet_var = tk.StringVar()
diet_menu = ttk.OptionMenu(input_frame, diet_var, *diets)
diet_menu.grid(row=1, column=1, sticky=tk.W)

update_button = ttk.Button(input_frame, text="Update Meals", command=update_meals)
update_button.grid(row=2, column=0, columnspan=2)

export_button = ttk.Button(input_frame, text="Export to CSV", command=export_grocery_list)
export_button.grid(row=3, column=0, columnspan=2)

# Create a label to display the nutritional information
nutrition_label = ttk.Label(input_frame, text="")
nutrition_label.grid(row=4, column=0, columnspan=2)

# Create the listbox to display the meal options
meal_list = tk.Listbox(list_frame, width=40, height=20)
meal_list.grid(row=0, column=0, sticky=tk.W+tk.E)
scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=meal_list.yview)
scrollbar.grid(row=0, column=1, sticky=tk.N+tk.S)
meal_list.configure(yscrollcommand=scrollbar.set)

# Bind the update_nutrition function to the listbox selection event
meal_list.bind('<<ListboxSelect>>', lambda event: update_nutrition())


# Start the main application loop
root.mainloop()


# Get user inputs
diet = input("Enter your dietary restriction (none, vegetarian, vegan, pescatarian, gluten-free, dairy-free): ")
cuisine = input("Enter the cuisine you want (Italian, Mexican, Indian, Chinese, Thai, Mediterranean): ")

# Filter meal options based on user preferences
filtered_meals = filter_meals(meal_options[cuisine], diet)

# Let the user select the meals they want to prepare
print("\nSelect the meals you want to prepare:")
for i, meal in enumerate(filtered_meals, start=1):
    print(f"{i}. {meal}")

selected_meal_indices = input("\nEnter the meal numbers separated by commas (e.g., 1,2,3): ").split(',')
selected_meals = [filtered_meals[int(index) - 1] for index in selected_meal_indices]

# Generate the grocery list (based on ingredients of selected meals)
grocery_list = set()
for meal in selected_meals:
    ingredients = meal_ingredients[meal]
    for ingredient in ingredients:
        grocery_list.add(ingredient)

# Print the grocery list
print("\nGrocery List:")
for item in grocery_list:
    print(f"- {item}")

# Display the nutritional information for the selected meals
print("\nNutritional Information for the Selected Meals:")
for meal in selected_meals:
    nutrition = meal_nutrition[meal]
    print("Nutritional information for {}: Calories: {}, Protein: {}g, Fat: {}g, Carbs: {}g".format(meal, nutrition["calories"], nutrition["protein"], nutrition["fat"], nutrition["carbs"]))

# Export the grocery list as a CSV file
filename = "grocery_list.csv"
with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Grocery List'])
    for item in grocery_list:
        writer.writerow([item])

print(f"\nGrocery list exported as {filename}")

# Export the grocery list as a CSV file
filename = "grocery_list.csv"
with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Grocery List'])
    for item in grocery_list:
        writer.writerow([item])

print(f"\nGrocery list exported as {filename}")



