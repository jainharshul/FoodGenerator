# FoodGenerator

Recipe Finder
This repository contains a Python script that helps you find recipes based on a given set of ingredients. It uses a CSV dataset of recipes and allows users to input ingredients to search for matching recipes. Once the recipes are found, the script displays the titles and instructions for the matching recipes, allowing the user to choose a recipe to follow.

Requirements
Python 3.x
Pandas library
Installation
Clone the repository to your local machine or download the script directly.

Ensure that you have Python 3.x installed on your system.

Install the required dependencies by running the following command:

shell
Copy code
pip install pandas
Usage
Open a terminal or command prompt and navigate to the directory containing the script.

Run the script using the following command:

shell
Copy code
python recipe_finder.py
The script will load the dataset and prompt you to enter ingredients. Provide a comma-separated list of ingredients and press Enter.

The script will search for recipes containing the given ingredients and display the titles of the matching recipes.

Choose a recipe by entering its corresponding number and pressing Enter.

The script will display the instructions for the chosen recipe.

Note: Please make sure to update the path to the CSV dataset in the script before running it. Modify the line:

python
Copy code
df = pd.read_csv('/Users/harshuljain/Desktop/dataset/full_dataset.csv')
Replace /Users/harshuljain/Desktop/dataset/full_dataset.csv with the path to your own dataset file.

Dataset
The script uses a CSV dataset containing recipes. The dataset should have the following structure:

title	ingredients	directions
Recipe 1	ingredient1, ingredient2, ...	Step 1: Instruction 1<br>Step 2: Instruction 2
Recipe 2	ingredient3, ingredient4, ...	Step 1: Instruction 1<br>Step 2: Instruction 2
...	...	...
Ensure that the dataset is in the same format and adjust the script accordingly if necessary.

Contributing
Contributions to this repository are welcome. If you encounter any issues, have suggestions for improvements, or would like to add new features, please feel free to submit a pull request.

License
This project is licensed under the MIT License.
