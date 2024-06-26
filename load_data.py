import json
from src import Category
from src.product import Product

products_file = 'data/products.json'
if __name__ == '__main__':
    with open(products_file) as file:
        data = json.load(file)

    categories = []
    # парсинг JSON-файла с созданием категорий и их продуктов
    for item in data:
        products_list = []
        for prd_item in item['products']:
            product = Product(**prd_item)
            products_list.append(product)
        category = Category(item['name'], item['description'], products_list)
        categories.append(category)

    # вывод полученных данных
    for ctg in categories:
        print(f"Название: {ctg.name}")
        print(f"Описание: {ctg.description}")
        print(f"Товары (количество:{len(ctg)}):")
        [print(f"  {prd}") for prd in ctg.products]
        print('-----')