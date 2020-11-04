from django.shortcuts import render
from .forms import UpdateFoodForm, DeleteFoodForm, InsertRestaurantForm, FoodPriceSelectorForm
# Create your views here.
def search(request):
    if request.method == 'POST':
        foodpriceform = FoodPriceSelectorForm(request.POST)
        if foodpriceform.is_valid():
            food_name =  foodpriceform.cleaned_data['foodName']
            restaurant_name = foodpriceform.cleaned_data['restaurantName']
            restaurant_address = foodpriceform.cleaned_data['restaurantAddress']
        
            print(food_name, restaurant_name, restaurant_address) #debug statement, just prints out the input in the terminal

    foodpriceform = FoodPriceSelectorForm()
    return render(request, 'selector/search.html', {'foodpriceform': foodpriceform})

def edit(request):
    upfoodform = UpdateFoodForm()
    delfoodform = DeleteFoodForm()
    inrestform = InsertRestaurantForm()
    return render(request, 'selector/edit.html', {'upfoodform': upfoodform, 'delfoodform': delfoodform, 'inrestform': inrestform})
