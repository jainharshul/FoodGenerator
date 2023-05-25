import pandas as pd
import random

print('python file working')

#data = pd.read_csv('/Users/harshuljain/Desktop/dataset') path to csv file for harshul

df = pd.read_csv('/Users/harshuljain/Desktop/dataset/full_dataset.csv')


def get_recipes_with_ingredients(df, ingredients):
    # Normalize the ingredients to lower case for consistent comparison
    ingredients = [ingredient.lower() for ingredient in ingredients]

    # This will hold all the indices of the recipes that contain the given ingredients
    recipe_indices = []

    # Iterate over the DataFrame
    for i, row in df.iterrows():
        # Convert the string of ingredients from the CSV into a list,
        # assuming the ingredients are comma separated
        recipe_ingredients = row['ingredients'].lower().split(',')
        # Check if any of the provided ingredients are in the recipe
        if any(ingredient in recipe_ingredients for ingredient in ingredients):
            recipe_indices.append(i)

    # Return the subset of the DataFrame that contains the recipes with the given ingredients
    return df.loc[recipe_indices]

# Let's say a user inputs these ingredients
user_ingredients = ['potato', 'onion', 'garlic']

# Use the function to get the recipes with the given ingredients
recipes = get_recipes_with_ingredients(df, user_ingredients)

# Print the titles of the recipes
for i, title in enumerate(recipes['title']):
    print(f"{i+1}. {title}")

# Ask the user to choose a recipe
recipe_number = int(input("\nEnter the number of the recipe you want to make: ")) - 1

# Print the instructions for the chosen recipe
chosen_recipe = recipes.iloc[recipe_number]
print("\nHere are the instructions for your chosen recipe:\n")
print(chosen_recipe['directions'])
