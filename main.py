"""
Recipe Manager - Main Program
"""

from manager import RecipeManager
from resources import APPLICATION_NAME, APPLICATION_VERSION

def create_sample_recipes(manager):
    """
    Create sample recipe data
    """
    # Italian Pasta
    pasta = manager.add_recipe("Spaghetti Carbonara", "Italian")
    pasta.add_ingredient("Spaghetti", 400, "g")
    pasta.add_ingredient("Eggs", 4, "pcs")
    pasta.add_ingredient("Bacon", 200, "g")
    pasta.add_ingredient("Parmesan cheese", 100, "g")
    pasta.add_instruction(1, "Cook spaghetti according to package directions")
    pasta.add_instruction(2, "Fry bacon until crispy")
    pasta.add_instruction(3, "Mix eggs with cheese")
    pasta.add_instruction(4, "Combine all ingredients")
    pasta.set_times(10, 20)
    pasta.set_servings(4)
    pasta.set_difficulty("Medium")
    pasta.add_rating(5)
    pasta.add_rating(4)
    
    # Chinese Stir Fry
    stirfry = manager.add_recipe("Chicken Stir Fry", "Chinese")
    stirfry.add_ingredient("Chicken breast", 500, "g")
    stirfry.add_ingredient("Bell peppers", 2, "pcs")
    stirfry.add_ingredient("Soy sauce", 3, "tbsp")
    stirfry.add_ingredient("Garlic", 3, "cloves")
    stirfry.add_instruction(1, "Cut chicken into strips")
    stirfry.add_instruction(2, "Chop vegetables")
    stirfry.add_instruction(3, "Stir fry chicken until cooked")
    stirfry.add_instruction(4, "Add vegetables and sauce")
    stirfry.set_times(15, 10)
    stirfry.set_servings(3)
    stirfry.set_difficulty("Easy")
    stirfry.add_rating(5)
    
    # Mexican Tacos
    tacos = manager.add_recipe("Beef Tacos", "Mexican")
    tacos.add_ingredient("Ground beef", 500, "g")
    tacos.add_ingredient("Taco shells", 8, "pcs")
    tacos.add_ingredient("Lettuce", 1, "head")
    tacos.add_ingredient("Cheese", 200, "g")
    tacos.add_instruction(1, "Brown the ground beef")
    tacos.add_instruction(2, "Season with taco seasoning")
    tacos.add_instruction(3, "Prepare toppings")
    tacos.add_instruction(4, "Assemble tacos")
    tacos.set_times(5, 15)
    tacos.set_servings(4)
    tacos.set_difficulty("Easy")
    tacos.add_rating(4)
    tacos.add_rating(5)
    
    print(f"Created {manager.get_recipe_count()} sample recipes")

def print_separator(char='=', length=70):
    """
    Print separator line
    """
    print(char * length)

def display_recipe(recipe):
    """
    Display recipe details
    """
    print(f"Recipe: {recipe.name}")
    print(f"Cuisine: {recipe.cuisine_type}")
    print(f"Difficulty: {recipe.difficulty}")
    print(f"Prep Time: {recipe.prep_time} min")
    print(f"Cook Time: {recipe.cook_time} min")
    print(f"Total Time: {recipe.get_total_time()} min")
    print(f"Servings: {recipe.servings}")
    print(f"Rating: {recipe.rating:.1f}/5 ({recipe.reviews_count} reviews)")
    print("")
    
    print("Ingredients:")
    for ing in recipe.ingredients:
        print(f"  - {ing['quantity']} {ing['unit']} {ing['ingredient']}")
    print("")
    
    print("Instructions:")
    for inst in recipe.instructions:
        print(f"  {inst['step']}. {inst['instruction']}")
    print("")

def main():
    """
    Main program execution
    """
    print_separator()
    print(f"{APPLICATION_NAME} v{APPLICATION_VERSION}")
    print_separator()
    print("")
    
    # Create manager
    manager = RecipeManager()
    
    # Add sample recipes
    print("Loading recipe collection...")
    create_sample_recipes(manager)
    print("")
    
    # Display statistics
    stats = manager.get_statistics()
    print_separator()
    print("Recipe Collection Statistics")
    print_separator()
    print(f"Total Recipes: {stats['total_recipes']}")
    print(f"Average Rating: {stats['average_rating']}/5")
    print(f"Average Time: {stats['average_time']} minutes")
    print(f"Total Cuisines: {stats['total_cuisines']}")
    print("")
    
    print("Difficulty Distribution:")
    for difficulty, count in stats['difficulty_distribution'].items():
        print(f"  {difficulty}: {count} recipes")
    print("")
    
    # Display top rated recipes
    print_separator()
    print("Top Rated Recipes")
    print_separator()
    top_recipes = manager.get_top_rated(3)
    for i, recipe in enumerate(top_recipes, 1):
        print(f"{i}. {recipe.name} - {recipe.rating:.1f}/5")
    print("")
    
    # Display quick recipes
    print_separator()
    print("Quick Recipes (under 30 minutes)")
    print_separator()
    quick = manager.get_quick_recipes(30)
    for recipe in quick:
        print(f"  {recipe.name} - {recipe.get_total_time()} min")
    print("")
    
    # Display recipes by cuisine
    print_separator()
    print("Recipes by Cuisine")
    print_separator()
    for cuisine in manager.get_all_cuisines():
        count = len(manager.filter_by_cuisine(cuisine))
        print(f"{cuisine}: {count} recipe(s)")
    print("")
    
    # Display full recipe details
    print_separator()
    print("Featured Recipe")
    print_separator()
    featured = manager.get_recipe("RCP0001")
    if featured:
        display_recipe(featured)
    
    # Generate shopping list
    print_separator()
    print("Shopping List (for selected recipes)")
    print_separator()
    shopping_list = manager.get_shopping_list(["RCP0001", "RCP0002"])
    for item, details in sorted(shopping_list.items()):
        print(f"  {details['quantity']} {details['unit']} {item}")
    print("")

if __name__ == "__main__":
    main()
