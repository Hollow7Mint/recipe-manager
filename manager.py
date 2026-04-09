"""
Recipe Manager
Manage and organize cooking recipes
"""

from recipe import Recipe

class RecipeManager:
    def __init__(self):
        self.recipes = {}
        self.next_id = 1
    
    def add_recipe(self, name, cuisine_type):
        """
        Add a new recipe
        """
        recipe_id = f"RCP{self.next_id:04d}"
        self.next_id += 1
        
        recipe = Recipe(recipe_id, name, cuisine_type)
        self.recipes[recipe_id] = recipe
        
        return recipe
    
    def get_recipe(self, recipe_id):
        """
        Get recipe by ID
        """
        return self.recipes.get(recipe_id)
    
    def delete_recipe(self, recipe_id):
        """
        Delete a recipe
        """
        if recipe_id in self.recipes:
            del self.recipes[recipe_id]
            return True
        return False
    
    def search_by_name(self, query):
        """
        Search recipes by name
        """
        query_lower = query.lower()
        results = []
        
        for recipe in self.recipes.values():
            if query_lower in recipe.name.lower():
                results.append(recipe)
        
        return results
    
    def filter_by_cuisine(self, cuisine_type):
        """
        Filter recipes by cuisine type
        """
        return [r for r in self.recipes.values() if r.cuisine_type == cuisine_type]
    
    def filter_by_time(self, max_minutes):
        """
        Filter recipes by maximum total time
        """
        return [r for r in self.recipes.values() if r.get_total_time() <= max_minutes]
    
    def filter_by_difficulty(self, difficulty):
        """
        Filter recipes by difficulty level
        """
        return [r for r in self.recipes.values() if r.difficulty == difficulty]
    
    def get_top_rated(self, limit=10):
        """
        Get top rated recipes
        """
        sorted_recipes = sorted(
            self.recipes.values(),
            key=lambda r: (r.rating, r.reviews_count),
            reverse=True
        )
        return sorted_recipes[:limit]
    
    def get_quick_recipes(self, max_time=30):
        """
        Get recipes that can be made quickly
        """
        return self.filter_by_time(max_time)
    
    def get_all_cuisines(self):
        """
        Get list of all cuisine types in collection
        """
        cuisines = set()
        for recipe in self.recipes.values():
            cuisines.add(recipe.cuisine_type)
        return sorted(list(cuisines))
    
    def get_statistics(self):
        """
        Get recipe collection statistics
        """
        if not self.recipes:
            return None
        
        total_recipes = len(self.recipes)
        avg_rating = sum(r.rating for r in self.recipes.values()) / total_recipes
        avg_time = sum(r.get_total_time() for r in self.recipes.values()) / total_recipes
        
        difficulty_count = {}
        for recipe in self.recipes.values():
            difficulty = recipe.difficulty
            difficulty_count[difficulty] = difficulty_count.get(difficulty, 0) + 1
        
        stats = {
            'total_recipes': total_recipes,
            'average_rating': round(avg_rating, 2),
            'average_time': round(avg_time, 1),
            'difficulty_distribution': difficulty_count,
            'total_cuisines': len(self.get_all_cuisines())
        }
        
        return stats
    
    def get_recipe_count(self):
        """
        Get total number of recipes
        """
        return len(self.recipes)
    
    def get_shopping_list(self, recipe_ids):
        """
        Generate shopping list for multiple recipes
        """
        shopping_list = {}
        
        for recipe_id in recipe_ids:
            recipe = self.get_recipe(recipe_id)
            if recipe:
                for ingredient in recipe.ingredients:
                    item = ingredient['ingredient']
                    qty = ingredient['quantity']
                    unit = ingredient['unit']
                    
                    if item in shopping_list:
                        shopping_list[item]['quantity'] += qty
                    else:
                        shopping_list[item] = {
                            'quantity': qty,
                            'unit': unit
                        }
        
        return shopping_list
