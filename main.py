# Домашнее задание по теме "Режимы открытия файлов"

class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self) -> str:
        try:
            with open(self.__file_name, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return ""

    def add(self, *products: Product):
        existing_products = self.get_products().splitlines()
        existing_names = {product.split(', ')[0] for product in existing_products}

        for product in products:
            if product.name not in existing_names:
                with open(self.__file_name, 'a') as file:
                    file.write(f'{product}\n')
            else:
                print(f'Продукт {product.name} уже есть в магазине')


# Пример работы программы
if __name__ == '__main__':
    s1 = Shop()

    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')  # Дубликат по названию

    print(p2)  # __str__

    s1.add(p1, p2, p3)  # Добавляем продукты
    print(s1.get_products())  # Выводим продукты из файла

