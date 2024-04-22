# import pandas as pd
# from fuzzywuzzy import process
# import re

# def load_recipes(file_path):
#     try:
#         return pd.read_csv(file_path)
#     except Exception as e:
#         print(f"An error occurred while loading the recipes: {e}")
#         return None

# def find_recipes_with_ingredients(available_ingredients, recipes_df):
#     matched_recipes = []
#     threshold = 85  # Fuzzy match threshold
#     min_matches_required = 5  # Minimum number of matching ingredients

#     for index, row in recipes_df.iterrows():
#         recipe_ingredients = set(map(str.strip, row['Cleaned_Ingredients'].split(',')))
#         matched_counts = {}  # To store how many times each ingredient matched

#         for user_ingredient in available_ingredients:
#             best_match, score = process.extractOne(user_ingredient, recipe_ingredients)
#             if score >= threshold:
#                 matched_counts[best_match] = matched_counts.get(best_match, 0) + 1

#         total_matches = sum(matched_counts.values())  # Total matched ingredients count
#         if total_matches >= min_matches_required:
#             matched_recipes.append((row['Title'], total_matches, row['Instructions'], row['Cleaned_Ingredients']))

#     matched_recipes.sort(key=lambda x: x[1], reverse=True)
#     return matched_recipes

# def merge_ingredients(ingredients_list):
#     merged_ingredients = []
#     continuation = False

#     for ingredient in ingredients_list:
#         ingredient = ingredient.strip()
#         if re.match(r'^(\d+[/\d]*|\(\d+)', ingredient):
#             merged_ingredients.append(ingredient)
#             continuation = False
#         else:
#             if continuation and merged_ingredients:
#                 merged_ingredients[-1] += f' {ingredient}'
#             else:
#                 merged_ingredients.append(ingredient)
#             continuation = True
    
#     return merged_ingredients

# recipes_df = load_recipes('csv_file/data.csv')

# if recipes_df is not None:
#     user_ingredients = input("Enter at least 8 ingredients you have, separated by commas: ").split(',')
#     user_ingredients = [ingredient.strip().lower() for ingredient in user_ingredients]

#     if len(user_ingredients) < 8:
#         print("Please enter at least 8 ingredients.")
#     else:
#         matched_recipes = find_recipes_with_ingredients(user_ingredients, recipes_df)
#         if matched_recipes:
#             print("Based on your ingredients, you can make:")
#             for idx, (recipe, count, _, _) in enumerate(matched_recipes, 1):
#                 if count >= 5:
#                     print(f"{idx}. {recipe} (with {count} of your ingredients)")
            
#             selection = input("\nEnter the number of the recipe you want to see the ingredients and instructions for: ")
#             if selection.isdigit():
#                 selected_index = int(selection) - 1
#                 if 0 <= selected_index < len(matched_recipes):
#                     title, _, instructions, ingredients_str = matched_recipes[selected_index]
#                     print(f"\nIngredients for '{title}':")
#                     ingredients = ingredients_str.strip("[]").replace("'", "").split(',')
#                     ingredients = merge_ingredients(ingredients)
#                     for i, ingredient in enumerate(ingredients, 1):
#                         print(f"{i}. {ingredient.strip()}")

#                     print(f"\nInstructions for '{title}':")
#                     steps = instructions.split('.')
#                     for i, step in enumerate(filter(None, steps), 1):
#                         print(f"{i}. {step.strip()}")
#                 else:
#                     print("Invalid selection. Please enter a number from the list.")
#             else:
#                 print("Please enter a valid number.")
#         else:
#             print("No recipes found with the given ingredients.")
# else:
#     print("Failed to load recipes.")

from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
from fuzzywuzzy import process
import re

app = Flask(__name__)

recipes_df = pd.read_csv('csv_file/data.csv')  # Load the data globally

def find_recipes_with_ingredients(available_ingredients, recipes_df):
    matched_recipes = []
    threshold = 85  # Fuzzy match threshold
    min_matches_required = 5  # Minimum number of matching ingredients

    for index, row in recipes_df.iterrows():
        recipe_ingredients = set(map(str.strip, row['Cleaned_Ingredients'].split(',')))
        matched_counts = {}

        for user_ingredient in available_ingredients:
            best_match, score = process.extractOne(user_ingredient, recipe_ingredients)
            if score >= threshold:
                matched_counts[best_match] = matched_counts.get(best_match, 0) + 1

        total_matches = sum(matched_counts.values())
        if total_matches >= min_matches_required:
            matched_recipes.append((index, row['Title'], total_matches))  # Use the DataFrame index as an identifier

    matched_recipes.sort(key=lambda x: x[2], reverse=True)  # Sort by count of matched ingredients
    return matched_recipes

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_ingredients = request.form['ingredients'].split(',')
        user_ingredients = [ingredient.strip().lower() for ingredient in user_ingredients]

        if len(user_ingredients) < 8:
            return render_template('index.html', error="Please enter at least 8 ingredients.")
        else:
            matched_recipes = find_recipes_with_ingredients(user_ingredients, recipes_df)
            return render_template('results.html', recipes=matched_recipes)
    return render_template('index.html')


@app.route('/recipe/<int:recipe_id>')
def recipe_detail(recipe_id):
    try:
        row = recipes_df.iloc[recipe_id]  # Directly access the recipe by DataFrame index
        ingredients_list = row['Cleaned_Ingredients'].strip("[]").replace("'", "").split(',')
        ingredients = merge_ingredients(ingredients_list)
        return render_template('recipe_detail.html', title=row['Title'], ingredients=ingredients, instructions=row['Instructions'])
    except IndexError:
        return redirect(url_for('index'))  # Redirect if the index is out of bounds

def merge_ingredients(ingredients_list):
    merged_ingredients = []
    continuation = False

    for ingredient in ingredients_list:
        ingredient = ingredient.strip()
        if re.match(r'^(\d+[/\d]*|\(\d+)', ingredient):
            merged_ingredients.append(ingredient)
            continuation = False
        else:
            if continuation and merged_ingredients:
                merged_ingredients[-1] += f' {ingredient}'
            else:
                merged_ingredients.append(ingredient)
            continuation = True

    return merged_ingredients

if __name__ == '__main__':
    app.run(debug=True) 
