input = open('input2.txt').read().splitlines()

n = len(input)
all_allergens = set()
foods = []
for line in input:
    ingredients, allergens = line.split(' (contains ')
    ingredients = set(ingredients.split(' '))
    allergens = set(allergens[:-1].split(', '))
    all_allergens |= allergens
    foods.append((ingredients, allergens))

dangerous_ingredients = []
while True:
    allergen_found = False
    for allergen in all_allergens:
        current_matches = set()
        for ingredients, allergens in foods:
            if allergen in allergens:
                if len(current_matches) == 0:
                    current_matches |= ingredients
                else:
                    current_matches &= ingredients
                    if len(current_matches) == 1:
                        allergen_found = True
                        break
        if allergen_found == True:
            all_allergens.remove(allergen)
            ingredient = current_matches.pop()
            dangerous_ingredients.append((ingredient, allergen))
            for ingredients, allergens in foods:
                if ingredient in ingredients:
                    ingredients.remove(ingredient)
                if allergen in allergens:
                    allergens.remove(allergen)
            break
    if allergen_found == False:
        break


dangerous_ingredients.sort(key=lambda x: x[1])
print(','.join(map(lambda x: x[0], dangerous_ingredients)))