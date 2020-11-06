from django.shortcuts import render
from .forms import UpdateFoodForm, DeleteFoodForm, InsertRestaurantForm, FoodPriceSelectorForm
from .models import Users, Restaurants, FoodItems, Ratings
from django.db import connection
# Create your views here.

def search(request):
    if request.method == 'POST':
        foodpriceform = FoodPriceSelectorForm(request.POST)
        if foodpriceform.is_valid():
            food_name =  foodpriceform.cleaned_data['foodName']
            restaurant_name = foodpriceform.cleaned_data['restaurantName']
            restaurant_address = foodpriceform.cleaned_data['restaurantAddress']
            restaurant_id = Restaurants.objects.get(restaurantName=str(restaurant_name), restaurant_address=str(restaurant_address))
#             query = '''select foodName, price
#                         from FoodItems
#                         where foodName = '{food_name}' and restaurantId = (select restaurantId from Restaurants where restaurantName = '{restaurant_name}' and restaurantAddress = '{restaurant_address}')
#                     '''.format(food_name=food_name, restaurant_name=restaurant_name, restaurant_address=restaurant_address)
            query = '''select foodName, price
                        from FoodItems
                        where foodName = '{food_name}' and restaurantId = {restaurant_id}
                    '''.format(food_name=food_name, restaurant_id=restaurant_id)
            res = FoodItems.objects.raw(query)
            context = {'res': res}
            return render(request, 'selector/search_results.html', context)
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
                with connection.cursor() as cursor:
                    cursor.execute("update FoodItems set price = price + 1 where foodName = {food_name} and vegetarian = {vegetarian}".format(food_name=food_name, vegetarian=vegetarian))
                print(food_name, vegetarian)
        elif "delete" in request.POST:
            deletefoodform = DeleteFoodForm(request.POST)
            if deletefoodform.is_valid():
                food_name = deletefoodform.cleaned_data['foodName']
                with connection.cursor() as cursor:
                    cursor.execute("delete from FoodItems where foodName = {food_name}".format(food_name=food_name))
                print(food_name)
        elif "insert" in request.POST:
            insertrestaurantform = InsertRestaurantForm(request.POST)
            if insertrestaurantform.is_valid():
                restaurant_name = insertrestaurantform.cleaned_data['restaurantName']
                restaurant_address= insertrestaurantform.cleaned_data['restaurantAddress']
                restaurant_zip = insertrestaurantform.cleaned_data['restaurantZip']
                with connection.cursor() as cursor:
                    cursor.execute('''insert into Restaurants(restaurantName, restaurantAddress, restaurantZip) 
                                      values ({restaurant_name}, {restaurant_address}, {restaurant_zip})'''.format(restaurant_name=restaurant_name, restaurant_address=restaurant_address, restaurant_zip=restaurant_zip))
                print(restaurant_name, restaurant_address, restaurant_zip)
    
    upfoodform = UpdateFoodForm()
    delfoodform = DeleteFoodForm()
    inrestform = InsertRestaurantForm()
    return render(request, 'selector/edit.html', {'upfoodform': upfoodform, 'delfoodform': delfoodform, 'inrestform': inrestform})
