from django import forms

class UpdateFoodForm(forms.Form):
    foodName = forms.CharField(label = 'Food Name')
    vegetarianStatus = forms.ChoiceField(label = 'Vegetarian Status', choices =[('vegetarian', 'Vegetarian'), ('vegan', 'Vegan'), ('none', 'None')])

class DeleteFoodForm(forms.Form):
    foodName = forms.CharField(label = 'Food Name')

class InsertRestaurantForm(forms.Form):
    restaurantName = forms.CharField(label = 'Restaurant Name')
    restarantAddress = forms.CharField(label = 'Restaurant Address') 
    restaurantNameZip = forms.IntegerField(label = 'Restaurant Zip')

class FoodPriceSelectorForm(forms.Form):
    foodName = forms.CharField(label = 'Food Name')
    restaurantName = forms.CharField(label = 'Restaurant Name')
    restaurantAddress = forms.CharField(label = 'Restaurant Address') 

