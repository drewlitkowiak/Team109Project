use food;

SELECT R.restaurantName, count(F.FoodID) AS amountFood
FROM Restaurants as R NATURAL JOIN FoodItems as F
WHERE F.cuisine = 'American'
GROUP BY R.restaurantId
ORDER BY amountFood DESC;

SELECT R.restaurantName, avg(F.price) as avgPrice
FROM Restaurants AS R NATURAL JOIN FoodItems as F
GROUP BY R.restaurantId
ORDER BY avgPrice DESC
