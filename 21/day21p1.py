input = open('input2.txt').read().splitlines()

n = len(input)
all_allergens = set()
foods = []
bad_food = set()
for line in input:
    ingredients, allergens = line.split(' (contains ')
    ingredients = set(ingredients.split(' '))
    allergens = set(allergens[:-1].split(', '))
    all_allergens |= allergens
    foods.append((ingredients, allergens))

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
                        bad_food |= current_matches
                        allergen_found = True
                        break
        if allergen_found == True:
            all_allergens.remove(allergen)
            ingredient = current_matches.pop()
            for ingredients, allergens in foods:
                if ingredient in ingredients:
                    ingredients.remove(ingredient)
                if allergen in allergens:
                    allergens.remove(allergen)
            break
    if allergen_found == False:
        break

for ingredients, allergens in foods:
    if len(allergens) != 0:
        bad_food |= ingredients

result = 0
for ingredients, allergens in foods:
    if len(allergens) == 0:
        for ingredient in ingredients:
            if ingredient not in bad_food:
                result += 1

print(result)