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
    allerfies2 = forms.ChoiceField(label = 'Allergies 2', choices =[('Dairy', 'Dairy'), ('Gluten', 'Gluten'), ('Seafood', 'Seafood'), ('No', 'No')])
    price = forms.FloatField(label = 'Price')

class InsertRestaurantForm(forms.Form):
    restaurantName = forms.CharField(label = 'Restaurant Name')
    restaurantAddress = forms.CharField(label = 'Restaurant Address') 
    restaurantZip = forms.IntegerField(label = 'Restaurant Zip')

class DeleteRestaurantForm(forms.Form):
    restaurantName = forms.CharField(label = 'Restaurant Name')
    restaurantAddress = forms.CharField(label = 'Restaurant Address') 

class InsertRatingsForm(forms.Form):
    email = forms.EmailField(label = 'Email')
    restaurantName = forms.CharField(label = 'Restaurant Name')
    restaurantAddress = forms.CharField(label = 'Restaurant Address') 
    rating = forms.IntegerField(label = 'Rating Number')

class FoodPriceSelectorForm(forms.Form):
    foodName = forms.CharField(label = 'Food Name')
    restaurantName = forms.CharField(label = 'Restaurant Name')
    restaurantAddress = forms.CharField(label = 'Restaurant Address') 

class UpdatePrefForm(forms.Form):
    email = forms.EmailField(label = 'Email')
    mostImportant = forms.ChoiceField(label = 'First Most Important Attribute', choices = [('Price', 'Price'), ('Location', 'Location'), ('Cuisine', 'Cuisine'), ('Vegetarian Status', 'Vegetarian Status'), ('Allergies', 'Allergies'), ('Something Familair', 'Something Familiar')])
    secondImportant = forms.ChoiceField(label = 'Second Most Important Attribute', choices = [('Price', 'Price'), ('Location', 'Location'), ('Cuisine', 'Cuisine'), ('Vegetarian Status', 'Vegetarian Status'), ('Allergies', 'Allergies'), ('Something Familair', 'Something Familiar')])
    thirdImportant = forms.ChoiceField(label = 'Third Most Important Attribute', choices = [('Price', 'Price'), ('Location', 'Location'), ('Cuisine', 'Cuisine'), ('Vegetarian Status', 'Vegetarian Status'), ('Allergies', 'Allergies'), ('Something Familair', 'Something Familiar')])
    fourthImportant = forms.ChoiceField(label = 'Fourth Most Important Attribute', choices = [('Price', 'Price'), ('Location', 'Location'), ('Cuisine', 'Cuisine'), ('Vegetarian Status', 'Vegetarian Status'), ('Allergies', 'Allergies'), ('Something Familair', 'Something Familiar')])
    fifthImportant = forms.ChoiceField(label = 'Fifth Most Important Attribute', choices = [('Price', 'Price'), ('Location', 'Location'), ('Cuisine', 'Cuisine'), ('Vegetarian Status', 'Vegetarian Status'), ('Allergies', 'Allergies'), ('Something Familair', 'Something Familiar')])
    sixthImportant = forms.ChoiceField(label = 'Sixth Most Important Attribute', choices = [('Price', 'Price'), ('Location', 'Location'), ('Cuisine', 'Cuisine'), ('Vegetarian Status', 'Vegetarian Status'), ('Allergies', 'Allergies'), ('Something Familair', 'Something Familiar')])
    favoriteRestaurant = forms.CharField(label = 'Favorite Restaurant')
    likedFood = forms.Charfield(label = 'Liked Food')

class RecomenderForm(forms.Form):
    email = forms.EmailField(label = 'Email')
    weather = forms.ChoiceField(label = 'Weather', choices=[('Good', 'Good'), ('Poor', 'Poor')])
    lowerprice = forms.FloatField(label = 'Lower Price')
    upperprice = forms.FloatField(label = 'Upper Price')
    cuisine = forms.ChoiceField(label = 'Cuisine', choices =[('American', 'American'), ('Mexican', 'Mexican'), ('Asian', 'Asian')])
    vegetarianStatus = forms.ChoiceField(label = 'Vegetarian Status', choices =[('Vegetarian', 'Vegetarian'), ('Vegan', 'Vegan'), ('No', 'No')])
    allergies1 = forms.ChoiceField(label = 'Allergies 1', choices =[('Dairy', 'Dairy'), ('Gluten', 'Gluten'), ('Seafood', 'Seafood'), ('No', 'No')])
    allerfies2 = forms.ChoiceField(label = 'Allergies 2', choices =[('Dairy', 'Dairy'), ('Gluten', 'Gluten'), ('Seafood', 'Seafood'), ('No', 'No')])
