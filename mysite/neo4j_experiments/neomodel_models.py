from neomodel import (config, StructuredNode, StringProperty, IntegerProperty, UniqueIdProperty, RelationshipTo)
from neomodel import config
import os

config.DATABASE_URL = os.environ['NEO4J_BOLT_URL']

class FoodItems(StructuredNode):
    FoodItem_id = UniqueIdProperty()
    name = StringProperty(required=True)

class Attributes(StructuredNode):
    attribute = StringProperty(unique_index=True, required=True)

class Restaurant(StructuredNode):
    Restaurant_uid = UniqueIdProperty()
    name = StringProperty(required=True)

class User(StructuredNode):
    name = StringProperty(required=True)
    uid = UniqueIdProperty()

    likedFoods = RelationshipTo(FoodItems, 'LIKES')
    mostFrequents = RelationshipTo(Restaurant, 'MOST_FREQUENTS')

    mostImportant = RelationshipTo(Attributes, 'MOST_IMPORTANT')
    secondImportant = RelationshipTo(Attributes, 'SECOND_IMPORTANT')
    thirdImportant = RelationshipTo(Attributes, 'THIRD_IMPORTANT')
    fourthImportant = RelationshipTo(Attributes, 'FOURTH_IMPORTANT')
    fifthImportant = RelationshipTo(Attributes, 'FIFTH_IMPORTANT')

