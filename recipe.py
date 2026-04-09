"""
Recipe Class
Represents a cooking recipe with ingredients and instructions
"""

class Recipe:
    def __init__(self, recipe_id, name, cuisine_type):
        self.recipe_id = recipe_id
        self.name = name
        self.cuisine_type = cuisine_type
        self.ingredients = []
        self.instructions = []
        self.prep_time = 0
        self.cook_time = 0
        self.servings = 1
        self.difficulty = "Medium"
        self.rating = 0.0
        self.reviews_count = 0
    
    def add_ingredient(self, ingredient, quantity, unit):
        """
        Add an ingredient to the recipe
        """
        self.ingredients.append({
            'ingredient': ingredient,
            'quantity': quantity,
            'unit': unit
        })
    
    def add_instruction(self, step_number, instruction):
        """
        Add a cooking instruction
        """
        self.instructions.append({
            'step': step_number,
            'instruction': instruction
        })
    
    def set_times(self, prep_minutes, cook_minutes):
        """
        Set preparation and cooking times
        """
        self.prep_time = prep_minutes
        self.cook_time = cook_minutes
    
    def set_servings(self, servings):
        """
        Set number of servings
        """
        if servings > 0:
            self.servings = servings
    
    def set_difficulty(self, difficulty):
        """
        Set recipe difficulty level
        """
        valid_levels = ["Easy", "Medium", "Hard"]
        if difficulty in valid_levels:
            self.difficulty = difficulty
    
    def add_rating(self, rating):
        """
        Add a user rating
        """
        if 1 <= rating <= 5:
            total = self.rating * self.reviews_count
            self.reviews_count += 1
            self.rating = (total + rating) / self.reviews_count
            return True
        return False
    
    def get_total_time(self):
        """
        Get total time (prep + cook)
        """
        return self.prep_time + self.cook_time
    
    def scale_recipe(self, new_servings):
        """
        Scale ingredient quantities for different servings
        """
        if new_servings <= 0 or self.servings <= 0:
            return None
        
        scale_factor = new_servings / self.servings
        scaled_ingredients = []
        
        for ingredient in self.ingredients:
            scaled_ingredients.append({
                'ingredient': ingredient['ingredient'],
                'quantity': ingredient['quantity'] * scale_factor,
                'unit': ingredient['unit']
            })
        
        return scaled_ingredients
    
    def to_dict(self):
        """
        Convert recipe to dictionary
        """
        return {
            'recipe_id': self.recipe_id,
            'name': self.name,
            'cuisine_type': self.cuisine_type,
            'ingredients': self.ingredients,
            'instructions': self.instructions,
            'prep_time': self.prep_time,
            'cook_time': self.cook_time,
            'total_time': self.get_total_time(),
            'servings': self.servings,
            'difficulty': self.difficulty,
            'rating': round(self.rating, 1),
            'reviews_count': self.reviews_count
        }
    
    def __str__(self):
        return f"{self.name} ({self.cuisine_type}) - {self.get_total_time()} min - {self.difficulty}"
