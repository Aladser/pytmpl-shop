from src.product import Product
from src.log_mixin import LogMixin
from src.non_positive_prd_quantity_exception import NonPositiveProductQuantityException


class Category(LogMixin):
    quantity = 0
    products_quantity = 0
    __name: str
    __description: str
    __products: list

    def __init__(self, name: str, description: str, products: list):
        """
        Категория
        :param name: имя
        :param products: товары
        :param description: описание
        """
        Category.quantity += 1
        Category.products_quantity += len(products)
        self.__name = name
        self.__description = description

        for prd in products:
            self.verify_product_quantity(prd)
        self.__products = products

        super().__init__()

    @property
    def name(self) -> str:
        return self.__name

    @property
    def description(self) -> str:
        return self.__description

    @property
    def products(self) -> list:
        return [str(prd) for prd in self.__products]

    def add_product(self, new_product):
        if not issubclass(type(new_product), Product):
            raise Exception(f"Объект {str(new_product)} должен быть экземляром класса Product или его наследника")
        self.verify_product_quantity(new_product)

        for i in range(0, len(self.__products)):
            if self.__products[i].name == new_product.name:
                # если такой продукт есть в категории
                self.__products[i].quantity += new_product.quantity
                if self.__products[i].price < new_product.price:
                    self.__products[i].price = new_product.price
                return

        self.__products.append(new_product)
        Category.products_quantity += 1

    @property
    def product_avg_price(self):
        """средняя цена товаров"""
        total_price = sum([prd.price for prd in self.__products])
        avg_price = 0

        try:
            avg_price = total_price / len(self.__products)
        except ZeroDivisionError as e:
            print(e)
        finally:
            return avg_price

    @staticmethod
    def verify_product_quantity(product: Product):
        """проверить количество добавляемого продукта"""
        if product.quantity <= 0:
            raise NonPositiveProductQuantityException(product.name)
        else:
            return True

    def __len__(self) -> int:
        prd_count = 0
        for prd in self.__products:
            prd_count += len(prd)
        return prd_count

    def __str__(self) -> str:
        return f"Название: {self.name}, количество продуктов: {self.__len__()} шт."
