from django.shortcuts import render
from .forms import UpdateFoodForm, DeleteFoodForm, InsertRestaurantForm, FoodPriceSelectorForm, InsertFoodForm, DeleteRestaurantForm, InsertRatingsForm, UpdatePrefForm, RecomenderForm
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
            query = '''SELECT *
                         FROM FoodItems AS F NATURAL JOIN Restaurants AS R
                         WHERE foodName = '{food_name}' and restaurantName = '{restaurant_name}' and restaurantAddress = '{restaurant_address}'
                     '''.format(food_name=food_name, restaurant_name=restaurant_name, restaurant_address=restaurant_address)
            res = FoodItems.objects.raw(query)

            context = {'res': res}
            return render(request, 'selector/search_results.html', context)
            print(food_name, restaurant_name, restaurant_address) #debug statement, just prints out the input in the terminal
            #this should probbaly redirect to a page do display the result of the search

    foodpriceform = FoodPriceSelectorForm()
    return render(request, 'selector/search.html', {'foodpriceform': foodpriceform})

def edit(request):
    if request.method == 'POST':
        if "updatefood" in request.POST:                        # Need to fix this for the new forms 
            updatefoodform = UpdateFoodForm(request.POST)   # 
            if updatefoodform.is_valid():
                food_name = updatefoodform.cleaned_data['foodName']
                newprice = updatefoodform.cleaned_data['price']
                with connection.cursor() as cursor:
                    cursor.execute("update FoodItems set price = '{newprice}' where foodName = '{food_name}' ".format(food_name=food_name, newprice=newprice))
                print(food_name, newprice)
        elif "deletefood" in request.POST:
            deletefoodform = DeleteFoodForm(request.POST)
            if deletefoodform.is_valid():
                food_name = deletefoodform.cleaned_data['foodName']
                with connection.cursor() as cursor:
                    cursor.execute("delete from FoodItems where foodName = '{food_name}'".format(food_name=food_name))
                print(food_name)
        elif "insertfood" in request.POST:
            insertfoodform = InsertFoodForm(request.POST)
            if insertfoodform.is_valid():
                food_name = insertfoodform.cleaned_data['foodName']
                rest_name = insertfoodform.cleaned_data['restaurantName']
                rest_addr = insertfoodform.cleaned_data['restaurantAddress']
                cuisine = insertfoodform.cleaned_data['cuisine']
                vegetarian = insertfoodform.cleaned_data['vegetarianStatus']
                allergy_1 = insertfoodform.cleaned_data['allergies1']
                allergy_2 = insertfoodform.cleaned_data['allergies2']
                price = insertfoodform.cleaned_data['price']
                query = '''SELECT *                                          
                            FROM Restaurants
                            WHERE restaurantName = '{restaurant_name}' and restaurantAddress = '{restaurant_address}'
                        '''.format( restaurant_name=rest_name, restaurant_address=rest_addr)            # the foreign key column in food items is restuarnt ID, so we need to query the restaurant table for the restaurnat ID based on the rest_name and rest_addr
                res = Restaurants.objects.raw(query)
                rest_id = 0
                for q in res:
                    rest_id = q.restaurantId  # res should only return one row, so this for loop will only run once and rest_id will be the id of the restaurant with the address and name 
                
                print(cuisine, rest_id, food_name, vegetarian, allergy1, allergy2, price) # another debug statment

                if allergy_1 != 'No' and allergy_2 != 'No' :
                    with connection.cursor() as cursor:                 # we have a bunch of if, elif statements here because allerigeis are optional fields, so they just cover the cases where both fields are filled, one of them is filled and both are empty
                        cursor.execute('''insert into FoodItems(restaurantID, cuisine, foodName, vegetarian, allergies1, allergies2, price ) 
                                        values ('{rest_id}', '{cuisine}', '{foodName}', '{vegetarian}','{allergy_1}','{allergy_2}','{price}' )'''.format(rest_id=rest_id, cuisine=cuisine, foodName=food_name, vegetarian=vegetarian, allergy_1 = allergy_1, allergy_2 = allergy_2, price = price ))
                elif allergy_1 != 'No' and allergy_2 == 'No' :
                    with connection.cursor() as cursor:
                        cursor.execute('''insert into FoodItems(restaurantID, cuisine, foodName, vegetarian, allergies1, price ) 
                                        values ('{rest_id}', '{cuisine}', '{foodName}', '{vegetarian}','{allergy_1}','{price}' )'''.format(rest_id=rest_id, cuisine=cuisine, foodName=food_name, vegetarian=vegetarian, allergy_1 = allergy_1, price = price))
                elif allergy_1 == 'No' and allergy_2 != 'No' :
                    with connection.cursor() as cursor:
                        cursor.execute('''insert into FoodItems(restaurantID, cuisine, foodName, vegetarian, allergies1, price ) 
                                        values ('{rest_id}', '{cuisine}', '{foodName}', '{vegetarian}','{allergy_1}', '{price}' )'''.format(rest_id=rest_id, cuisine=cuisine, foodName=food_name, vegetarian=vegetarian, allergy_1 = allergy_2, price = price ))
                else:
                     with connection.cursor() as cursor:
                        cursor.execute('''insert into FoodItems(restaurantID, cuisine, foodName, vegetarian, price ) 
                                        values ('{rest_id}', '{cuisine}', '{foodName}', '{vegetarian}','{price}' )'''.format(rest_id=rest_id, cuisine=cuisine, foodName=food_name, vegetarian=vegetarian, price = price ))
        elif "insertrest" in request.POST:
            insertrestaurantform = InsertRestaurantForm(request.POST)
            if insertrestaurantform.is_valid():
                restaurant_name = insertrestaurantform.cleaned_data['restaurantName']
                restaurant_address= insertrestaurantform.cleaned_data['restaurantAddress']
                restaurant_zip = insertrestaurantform.cleaned_data['restaurantZip']
                with connection.cursor() as cursor:
                    cursor.execute('''insert into Restaurants(restaurantName, restaurantAddress, restaurantZip) 
                                      values ('{restaurant_name}', '{restaurant_address}', '{restaurant_zip}')'''.format(restaurant_name=restaurant_name, restaurant_address=restaurant_address, restaurant_zip=restaurant_zip))
                print(restaurant_name, restaurant_address, restaurant_zip)
        elif "deleterest" in request.POST:
            deleterestform = DeleteRestaurantForm(request.POST)
            if deleterestform.is_valid():
                rest_name = deleterestform.cleaned_data['restaurantName']
                rest_addr = deleterestform.cleaned_data['restaurantAddress']
                with connection.cursor() as cursor:
                    cursor.execute("delete from Restaurants where restaurantName = '{rest_name}' and restaurantAddress = '{rest_addr}' ".format(rest_name=rest_name, rest_addr = rest_addr))
                print(food_name)

        elif "insertrat" in request.POST:     # insert ratings
            insertratform = InsertRatingsForm(request.POST)
            if insertratform.is_valid():
                user_email = insertratform.cleaned_data['email']
                rest_name = insertratform.cleaned_data['restaurantName']
                rest_addr = insertratform.cleaned_data['restaurantAddress']
                rating = insertratform.cleaned_data['rating']
                query = '''SELECT *                                          
                            FROM Restaurants
                            WHERE restaurantName = '{restaurant_name}' and restaurantAddress = '{restaurant_address}'
                        '''.format( restaurant_name=rest_name, restaurant_address=rest_addr)   # we need both userID and the restaurantID to make the insertion, so we need to query for those 
                res = Restaurants.objects.raw(query)
                rest_id = 0
                for q in res:
                    rest_id = q.restaurantId

                query = '''SELECT *                                          
                            FROM Users
                            WHERE userEmail = '{user_email}'
                        '''.format(user_email=user_email)       # querying for userID using the email and putting the Id into user_id
                use = Users.objects.raw(query)
                user_id = 0
                for p in use:
                    user_id = p.userID

                with connection.cursor() as cursor: # now we insert 
                    cursor.execute('''insert into Ratings(userID, restaurantID, ratingNum) 
                                      values ('{user_id}', '{rest_id}', '{rating}')'''.format(user_id=user_id, rest_id=rest_id, rating=rating))


    upfoodform = UpdateFoodForm()
    delfoodform = DeleteFoodForm()
    infoodform = InsertFoodForm()
    inrestform = InsertRestaurantForm()
    delrestform = DeleteRestaurantForm()
    inratform = InsertRatingsForm()
    return render(request, 'selector/edit.html', {'upfoodform': upfoodform, 'delfoodform': delfoodform, 'inrestform': inrestform, 'infoodform': infoodform, 'delrestform': delrestform, 'inratform': inratform })

def prefs(request):     # made a new page and view fucntion for updating the Neo4J db, 
    if request.method == 'POST':
        updateprefform = UpdatePrefForm(request.POST)
        if updateprefform.is_valid:
            email = updateprefform.cleaned_data['email']
            attr1 = updateprefform.cleaned_data['mostImportant']
            attr2 = updateprefform.cleaned_data['secondmportant']
            attr3 = updateprefform.cleaned_data['thirdImportant']
            attr4 = updateprefform.cleaned_data['fourthImportant']
            attr5 = updateprefform.cleaned_data['fifthImportant']
            attr6 = updateprefform.cleaned_data['sixthImportant']
            fav_rest = updateprefform.cleaned_data['favoriteRestaurant']
            liked_food = updateprefform.cleaned_data['likedFood']
    # need to hook up Neo4j and do then insert this data

    upprefform = UpdatePrefForm()
    return render(request, 'selector/prefs.html', {'upprefform': upprefform})

def rec(request):       # form for the recommender, needs to connect to Neo4j and sql db's
    if request.method == 'POST':
        recomenderform = RecomenderForm(request.POST)
        if recomenderform.is_valid:
            email = recomenderform.cleaned_data['email']
            weather = recomenderform.cleaned_data['weather']
            # now need to conenct to DB's to query

    recform = RecomenderForm()
    return render(request, 'selector/rec.html', {'recform' : recform})
