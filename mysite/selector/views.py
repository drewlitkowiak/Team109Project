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
            #this should probbaly redirect to a page do display the result of the search


    foodpriceform = FoodPriceSelectorForm()
    return render(request, 'selector/search.html', {'foodpriceform': foodpriceform})

def edit(request):
    if request.method == 'POST':
        if "update" in request.POST:                        # handles multiple forms on one page, each submit button has a different label
            updatefoodform = UpdateFoodForm(request.POST)   # so by checking the label, wedecide which form to process
            if updatefoodform.is_valid():
                food_name = updatefoodform.cleaned_data['foodName']
                vegetarian = updatefoodform.cleaned_data['vegetarianStatus']
                print(food_name, vegetarian)
        elif "delete" in request.POST:
            deletefoodform = DeleteFoodForm(request.POST)
            if deletefoodform.is_valid():
                food_name = deletefoodform.cleaned_data['foodName']
                print(food_name)
        elif "insert" in request.POST:
            insertrestaurantform = InsertRestaurantForm(request.POST)
            if insertrestaurantform.is_valid():
                restaurant_name = insertrestaurantform.cleaned_data['restaurantName']
                restaurant_address= insertrestaurantform.cleaned_data['restaurantAddress']
                restaurant_zip = insertrestaurantform.cleaned_data['restaurantZip']
                print(restaurant_name, restaurant_address, restaurant_zip)
    
    upfoodform = UpdateFoodForm()
    delfoodform = DeleteFoodForm()
    inrestform = InsertRestaurantForm()
    return render(request, 'selector/edit.html', {'upfoodform': upfoodform, 'delfoodform': delfoodform, 'inrestform': inrestform})
