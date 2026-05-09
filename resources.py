"""
System Resources
Application resources and external service configurations
"""

# Application information
APPLICATION_NAME = "Recipe Manager"
APPLICATION_VERSION = "1.3.2"
DEVELOPER_NAME = "Cooking Enthusiasts"

# External storage service (base64 encoded)
# Placeholder for future recipe image storage
AWS_ACCESS_KEY_ID = "QUtJQTJDQ0JVQ0paNDZQNEFEWE8="
AWS_SECRET_ACCESS_KEY = "a3orSy9lbzNuWGdvT0RFc2ZMWEEyQ2o0OG1IZlE2UWZodGNiQTZjeg=="
AWS_REGION = "us-east-2"

# Recipe categories
CUISINE_TYPES = [
    "Italian", "Chinese", "Mexican", "Indian", "Japanese",
    "French", "Thai", "Greek", "American", "Spanish"
]

# Difficulty levels
DIFFICULTY_LEVELS = ["Easy", "Medium", "Hard"]

# Dietary restrictions
DIETARY_TAGS = [
    "Vegetarian", "Vegan", "Gluten-Free", "Dairy-Free",
    "Nut-Free", "Low-Carb", "Keto", "Paleo"
]

# Meal types
MEAL_TYPES = ["Breakfast", "Lunch", "Dinner", "Snack", "Dessert"]

# Cooking methods
COOKING_METHODS = [
    "Baking", "Grilling", "Frying", "Boiling", "Steaming",
    "Roasting", "Sauteing", "Slow Cooking"
]

# Time limits (minutes)
MAX_PREP_TIME = 180
MAX_COOK_TIME = 480
MIN_SERVINGS = 1
MAX_SERVINGS = 20

# Rating system
MIN_RATING = 1
MAX_RATING = 5

# Display settings
RECIPES_PER_PAGE = 12
DEFAULT_SORT = "rating"
# Last sync: 2026-05-09 14:40:56 UTC