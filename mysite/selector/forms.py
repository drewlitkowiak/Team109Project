from django import forms

class UpdateFoodForm(forms.Form):
    foodName = forms.CharField(label = 'Food Name')
    vegetarianStatus = forms.ChoiceField(label = 'Vegetarian Status', choices =[('Vegetarian', 'Vegetarian'), ('Vegan', 'Vegan'), ('No', 'No')])

class DeleteFoodForm(forms.Form):
    foodName = forms.CharField(label = 'Food Name')

class InsertRestaurantForm(forms.Form):
    restaurantName = forms.CharField(label = 'Restaurant Name')
    restaurantAddress = forms.CharField(label = 'Restaurant Address') 
    restaurantZip = forms.IntegerField(label = 'Restaurant Zip')

class FoodPriceSelectorForm(forms.Form):
    foodName = forms.CharField(label = 'Food Name')
    restaurantName = forms.CharField(label = 'Restaurant Name')
    restaurantAddress = forms.CharField(label = 'Restaurant Address') 

