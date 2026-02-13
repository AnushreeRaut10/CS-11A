def menu(item, quan, **restaurant):
    restaurant['Item'] = item
    restaurant['Quantity'] = quan
    return restaurant

restaurant = menu('Soup', 1, Location='Seattle', zipcode='98109')
print(restaurant)
    