def format_ingredient(ingredient: str):
    ing_list = ingredient.split(' | ')
    return {'ingredient_name': ing_list[0], 'quantity': int(ing_list[1]), 'measure': ing_list[2]}


def read_dish_ingredients(cook_book_file):
    ingredients_list = []
    for _ in range(int(cook_book_file.readline().strip())):
        ingredient = cook_book_file.readline().strip()
        ingredients_list.append(format_ingredient(ingredient))
    return ingredients_list


def read_cook_book(cb_file_name: str = 'recipes.txt'):
    cook_book = {}
    with open(cb_file_name, encoding='UTF8') as cb_file:
        while True:
            dish = cb_file.readline().strip()
            if dish:
                cook_book[dish] = read_dish_ingredients(cb_file)
            else:
                break
            if cb_file.readline() != '\n':
                break
    return cook_book


def main():
    cook_book = read_cook_book()
    print(*cook_book.items(), sep='\n')
    print(len(cook_book))
    pass


if __name__ == '__main__':
    main()
