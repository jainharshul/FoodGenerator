## Sous Chef
Sous Chef is a Flask-based web application designed to help users find recipes based on the ingredients they have available. The application uses fuzzy string matching to suggest recipes that closely match the user's ingredients, providing a convenient solution for meal planning.

## Features
1. Ingredient-Based Recipe Search: Input a list of ingredients you have, and the app will suggest recipes you can make.
2. Fuzzy Matching: The app uses FuzzyWuzzy to match ingredients, allowing for slight spelling errors or variations.
3. Recipe Details: View detailed instructions and ingredient lists for each recipe.
4. User-Friendly Interface: Simple and intuitive web interface for easy navigation.

## Installation
1. Clone the repository:
- ``` git clone https://github.com/yourusername/sous-chef.git ```
2. Navigate to the project directory:
- ```cd sous-chef```
3. Install dependencies:
- ```pip install -r requirements.tx```
4. Run the application:
- ```python app.py```
5. Access the application:
- Open your web browser and go to http://127.0.0.1:5000/.

## Usage
1. Enter ingredients: Input a comma-separated list of ingredients in the search box.
2. View results: See a list of recipes that match your ingredients.
3. View recipe details: Click on a recipe title to view detailed instructions and ingredient lists.

## Files
1. app.py: The main Flask application.
2. templates/: Directory containing HTML templates.
3. csv_file/data.csv: The CSV file containing recipe data.
4. requirements.txt: List of Python dependencies.

## Technologies
1. Programming Language: Python
2. Framework: Flask
3. Libraries:
 - pandas
 - FuzzyWuzzy
 - re (Regular Expressions)
 - 
## Evaluation
The application has been tested with various ingredient sets to ensure accurate and relevant recipe suggestions.

## Future Enhancements
- User Accounts: Implement personalized recipe suggestions based on user preferences.
- Enhanced Matching: Improve the ingredient matching algorithm for even better suggestions.
- Mobile Application: Develop a mobile app for better accessibility.
