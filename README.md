## Sous Chef
Sous Chef is a Flask-based web application designed to help users find recipes based on the ingredients they have available. The application uses fuzzy string matching to suggest recipes that closely match the user's ingredients, providing a convenient solution for meal planning.

Features
Ingredient-Based Recipe Search: Input a list of ingredients you have, and the app will suggest recipes you can make.
Fuzzy Matching: The app uses FuzzyWuzzy to match ingredients, allowing for slight spelling errors or variations.
Recipe Details: View detailed instructions and ingredient lists for each recipe.
User-Friendly Interface: Simple and intuitive web interface for easy navigation.
Installation
Clone the repository:
bash
Copy code
git clone https://github.com/yourusername/sous-chef.git
Navigate to the project directory:
bash
Copy code
cd sous-chef
Install dependencies:
Copy code
pip install -r requirements.txt
Prepare the data:
Ensure your recipe data is available in csv_file/data.csv.
Run the application:
Copy code
python app.py
Access the application:
Open your web browser and go to http://127.0.0.1:5000/.
Usage
Go to the homepage: The default route is /.
Enter ingredients: Input a comma-separated list of ingredients in the search box.
View results: See a list of recipes that match your ingredients.
View recipe details: Click on a recipe title to view detailed instructions and ingredient lists.
Files
app.py: The main Flask application.
templates/: Directory containing HTML templates.
csv_file/data.csv: The CSV file containing recipe data.
requirements.txt: List of Python dependencies.
Technologies
Programming Language: Python
Framework: Flask
Libraries:
pandas
FuzzyWuzzy
re (Regular Expressions)
Evaluation
The application has been tested with various ingredient sets to ensure accurate and relevant recipe suggestions. User feedback has been positive, highlighting the convenience and accuracy of the application.

Future Enhancements
User Accounts: Implement personalized recipe suggestions based on user preferences.
Enhanced Matching: Improve the ingredient matching algorithm for even better suggestions.
Mobile Application: Develop a mobile app for better accessibility.
