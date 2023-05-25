# Recipe Finder

This repository contains a Python script that helps you find recipes based on a given set of ingredients. It uses a CSV dataset of recipes and allows users to input ingredients to search for matching recipes. Once the recipes are found, the script displays the titles and instructions for the matching recipes, allowing the user to choose a recipe to follow.

## Requirements

- Python 3.x
- Pandas library

## Installation

1. Clone the repository to your local machine or download the script directly.
2. Ensure that you have Python 3.x installed on your system.
3. Install the required dependencies by running the following command:


## Usage

1. Open a terminal or command prompt and navigate to the directory containing the script.
2. Run the script using the following command:

python recipe_finder.py


3. The script will load the dataset and prompt you to enter ingredients. Provide a comma-separated list of ingredients and press Enter.
4. The script will search for recipes containing the given ingredients and display the titles of the matching recipes.
5. Choose a recipe by entering its corresponding number and pressing Enter.
6. The script will display the instructions for the chosen recipe.

**Note:** Please make sure to update the path to the CSV dataset in the script before running it. Modify the line:

```python
df = pd.read_csv('/Users/harshuljain/Desktop/dataset/full_dataset.csv')

Replace /Users/harshuljain/Desktop/dataset/full_dataset.csv with the path to your own dataset file.
