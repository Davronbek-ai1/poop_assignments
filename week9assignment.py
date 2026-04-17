from dataclasses import dataclass, field

@dataclass
class Ingredient:
    name: str
    grams: float
    calories_per_gram: float

    def total_calories(self) -> float:
        return self.grams * self.calories_per_gram
    
@dataclass
class Recipe:
    title: str
    servings: int
    ingredients: list = field(default_factory=lambda: [])
    total_calories: float = field(init=False)

    def __post_init__(self):
        self.total_calories = sum(ing.total_calories() for ing in self.ingredients)

    def refreshing(self):
        self.total_calories = sum(ing.total_calories() for ing in self.ingredients)
    
    def add_ingredient(self, ingredient: Ingredient):
        self.ingredients.append(ingredient)
        self.refreshing()

    def calories_per_serving(self) -> float:
        return self.total_calories / self.servings
    
    def scale(self, new_servings: int):
        for ing in self.ingredients:
            ing.grams *= new_servings/self.servings
        self.servings = new_servings
        self.refreshing()

    def display(self) -> str:
        lines  = [f"{self.title} ({self.servings} servings)"]
        for ing in self.ingredients:
            lines.append(f"  {ing.name}: {ing.grams}g ({ing.total_calories()} cal)")
        lines.append(f"Per serving: {self.calories_per_serving()} cal\n")
        return "\n".join(lines)

r = Recipe("Pancakes", 4)
r.add_ingredient(Ingredient("Flour", 200.0, 3.64))
r.add_ingredient(Ingredient("Milk", 300.0, 0.42))
r.add_ingredient(Ingredient("Egg", 100.0, 1.55))

print(r.total_calories)
print(r.calories_per_serving())
print(r.display())

r.scale(2)
print(r.display())
