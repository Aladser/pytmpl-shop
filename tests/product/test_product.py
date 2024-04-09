import pytest
from classes import Product, Smartphone, Grass


@pytest.fixture
def product():
    return Product(name='Хлеб', description="товар", price=10, quantity=5)


def test_init(product):
    assert product.name == 'Хлеб'
    assert product.price == 10
    assert product.quantity == 5
    assert len(product) == 5
    with pytest.raises(Exception):
        assert product.quantity == -5
    assert product.description == "товар"
    print(f"\n{product}", end='')


def test_price(product):
    price = 15
    # установка новой цены
    product.price = price
    assert product.price == price
    # нулевая цена
    with pytest.raises(Exception):
        product.price = 0


def test_create(product):
    title = 'яблоко'
    price = 11.5
    count = 3
    description = 'фрукт'
    product = Product.create({'name': title, 'price': price, 'quantity': count, 'description': description})
    assert product.name == title
    assert product.price == price
    assert product.quantity == count
    assert product.description == description


def test_add():
    grass_params = {
        'name': 'зеленая',
        'price': 10,
        'quantity': 5,
        'description': "товар 2",
        'country_manufacturer': 1,
        'germination_period': 2,
        'color': 'red'
    }
    smrt_params = {
        'name': 'Xiaomi',
        'price': 40000,
        'quantity': 3,
        'description': 'смартфон выполнен в корпусе серого цвета и предлагает мощные характеристики для комфортного решения разных задач',
        'perfomance': 687373,
        'model': '12X',
        'RAM': '32 Гб',
        'color': 'зеленый'
    }
    grass_1 = Grass(**grass_params)
    grass_2 = Grass(**grass_params)
    smartphone = Smartphone(**smrt_params)
    prd = Product(name='Хлеб', description="товар", price=20, quantity=5)
    # один тип
    assert grass_1 + grass_2 == 100
    # разные типы
    with pytest.raises(Exception):
        grass_1 + smartphone
    # родитель и наследник
    with pytest.raises(Exception):
        assert prd + grass_1 == 150
