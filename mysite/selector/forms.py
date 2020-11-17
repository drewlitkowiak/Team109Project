from django import forms
#added several new forms, and changed some old ones, so need to chnage views.py
class UpdateFoodForm(forms.Form):
    foodName = forms.CharField(label = 'Food Name')
    price = forms.FloatField(label = 'New Price')

class DeleteFoodForm(forms.Form):
    foodName = forms.CharField(label = 'Food Name')


class InsertFoodForm(forms.Form):   
    foodName = forms.CharField(label = 'Food Name')
    restaurantName = forms.CharField(label = 'Restaurant Name')
    restaurantAddress = forms.CharField(label = 'Restaurant Address')
    cuisine = forms.ChoiceField(label = 'Cuisine', choices =[('American', 'American'), ('Mexican', 'Mexican'), ('Asian', 'Asian')])
    vegetarianStatus = forms.ChoiceField(label = 'Vegetarian Status', choices =[('Vegetarian', 'Vegetarian'), ('Vegan', 'Vegan'), ('No', 'No')])
    allergies1 = forms.ChoiceField(label = 'Allergies 1', choices =[('Dairy', 'Dairy'), ('Gluten', 'Gluten'), ('Seafood', 'Seafood'), ('No', 'No')])
    allerfies2 = forms.ChoiceField(label = 'Allergies 1', choices =[('Dairy', 'Dairy'), ('Gluten', 'Gluten'), ('Seafood', 'Seafood'), ('No', 'No')])
    price = forms.FloatField(label = 'Price')

class InsertRestaurantForm(forms.Form):
    restaurantName = forms.CharField(label = 'Restaurant Name')
    restaurantAddress = forms.CharField(label = 'Restaurant Address') 
    restaurantZip = forms.IntegerField(label = 'Restaurant Zip')

class DeleteRestaurantForm(forms.Form):
    restaurantName = forms.CharField(label = 'Restaurant Name')
    restaurantAddress = forms.CharField(label = 'Restaurant Address') 
    restaurantZip = forms.IntegerField(label = 'Restaurant Zip')

class InsertRatingsForm(forms.Form):
    email = forms.EmailField(label = 'Email')
    restaurantName = forms.CharField(label = 'Restaurant Name')
    restaurantAddress = forms.CharField(label = 'Restaurant Address') 
    rating = forms.IntegerField(label = 'Rating Number')

class FoodPriceSelectorForm(forms.Form):
    foodName = forms.CharField(label = 'Food Name')
    restaurantName = forms.CharField(label = 'Restaurant Name')
    restaurantAddress = forms.CharField(label = 'Restaurant Address') 

