from neomodel import (config, StructuredNode, StringProperty, IntegerProperty, UniqueIdProperty, RelationshipTo)
from neomodel import config
import os

config.DATABASE_URL = os.environ['NEO4J_BOLT_URL']

class NeoFoodItems(StructuredNode):
    FoodItem_id = UniqueIdProperty()
    name = StringProperty(required=True)

class NeoAttributes(StructuredNode):
    attribute = StringProperty(unique_index=True, required=True)

class NeoRestaurant(StructuredNode):
    Restaurant_uid = UniqueIdProperty()
    name = StringProperty(required=True)

class NeoUser(StructuredNode):
    name = StringProperty(required=True)
    uid = UniqueIdProperty()

    likedFoods = RelationshipTo(NeoFoodItems, 'LIKES')
    mostFrequents = RelationshipTo(NeoRestaurant, 'MOST_FREQUENTS')

    mostImportant = RelationshipTo(NeoAttribute, 'MOST_IMPORTANT')
    secondImportant = RelationshipTo(NeoAttribute, 'SECOND_IMPORTANT')
    thirdImportant = RelationshipTo(NeoAttribute, 'THIRD_IMPORTANT')
    fourthImportant = RelationshipTo(NeoAttribute, 'FOURTH_IMPORTANT')
    fifthImportant = RelationshipTo(NeoAttribute, 'FIFTH_IMPORTANT')

