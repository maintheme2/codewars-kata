def cakes(recipe, available):
    utilizable = {}
    for key in recipe.keys():
        utilizable[key] = available[key]
    
    result = []
    for key in utilizable:
        amount = 0
        while utilizable[key] >= recipe[key]:
            amount += 1
            utilizable[key] -= recipe[key]
        result.append(amount)

    return min(result), utilizable, result

print(cakes({'cream': 1, 'flour': 3, 'sugar': 1, 'milk': 1, 'oil': 1, 'eggs': 1}, {'sugar': 1, 'eggs': 1, 'flour': 3, 'cream': 1, 'oil': 1, 'milk': 1}))