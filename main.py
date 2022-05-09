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


def read_dinner_menu(dinner_menu_file_name: str = 'dinner_menu.txt'):
    with open(dinner_menu_file_name, encoding='UTF8') as dinner_menu_file:
        dinner_menu_list = []
        for line in dinner_menu_file:
            dinner_menu_list.append(line.strip())
    return dinner_menu_list[:-1], int(dinner_menu_list[-1])


def get_shop_list_by_dishes(dishes: list, persons: int):
    cook_book = read_cook_book()
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                shop_list.setdefault(ingredient['ingredient_name'], {'measure': ingredient['measure'], 'quantity': 0})
                shop_list[ingredient['ingredient_name']]['quantity'] += ingredient['quantity'] * persons
    return shop_list


def main():
    get_shop_list_by_dishes(*read_dinner_menu())
    pass


if __name__ == '__main__':
    main()
