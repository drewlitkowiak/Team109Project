from django.db import models
from neomodel import (config, StructuredNode, StringProperty, IntegerProperty, EmailProperty, UniqueIdProperty, RelationshipTo)
# Create your models here.


class Users(models.Model):
    userID = models.BigAutoField(primary_key = True)
    userName = models.CharField(max_length=255)
    userEmail = models.EmailField(max_length=255)
    userZip = models.IntegerField(default=61820)

    class Meta:
        db_table = 'Users'

    def __str__(self):
        return str(self.userID) + '|' + str(self.userName)


class Restaurants(models.Model):
    restaurantId = models.BigAutoField(primary_key=True)
    restaurantName = models.CharField(max_length=255)
    restaurantAddress = models.CharField(max_length=255)
    restaurantZip = models.IntegerField(default=61820)

    class Meta:
        db_table = 'Restaurants'

    def __str__(self):
        return self.restaurantName


class Ratings(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurants, on_delete=models.CASCADE)
    ratingNum = models.IntegerField()

    class Meta:
        db_table = 'Ratings'


class FoodItems(models.Model):
    foodID = models.BigAutoField(primary_key=True)
    restaurant = models.ForeignKey(Restaurants, on_delete=models.CASCADE)
    cuisine = models.CharField(max_length=255)
    foodName = models.CharField(max_length=255)
    vegetarian = models.CharField(max_length=255)
    allergies1 = models.CharField(max_length=255)
    allergies2 = models.CharField(max_length=255)
    price = models.FloatField()

    class Meta:
        db_table = 'FoodItems'

# neo4j nodes defined below here

#class NeoUser(StructuredNode):
    #uid = UniqueIdProperty()
    #email = EmailProperty(required = True)
    #important1 = RelationshipTo('Attribute', 'Most_Important')
    #important2 = RelationshipTo('Attribute', 'Second_Important')
    #important3 = RelationshipTo('Attribute', 'Third_Important')
    #important4 = RelationshipTo('Attribute', 'Fourth_Important')
    #important5 = RelationshipTo('Attribute', 'Fifth_Important')
    #important6 = RelationshipTo('Attribute', 'Sixth_Important')
    #favrest = RelationshipTo('NeoRestaurant', 'Favorite_Restaurant')
    #likedfood = RelationshipTo('NeoFoodItem', 'Liked_Food_Item')
#class Attribute(StructuredNode):
    #attrName =  StringProperty(required = True)

#class NeoFoodItem(StructuredNode):
    #foodName = StringProperty(required = True)

#class NeoRestaurant(StructuredNode):
    #restName = StringProperty(required = True)
