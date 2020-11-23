from neomodel_models import *


#food = FoodItems(name = "Taco").save()

#print(FoodItems.nodes.all())


user = NeoUser(email = "60@demo.net").save()
print(NeoUser.nodes.all())
