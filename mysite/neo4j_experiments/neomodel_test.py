from neomodel_models import *


food = FoodItems(name = "Taco").save()

print(FoodItems.nodes.all())
