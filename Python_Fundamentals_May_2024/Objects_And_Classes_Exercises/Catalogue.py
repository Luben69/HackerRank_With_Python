class Catalogue:
    def __init__(self, name: str):
        self.name = name
        self.products = []

    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        return [el for el in self.products if el[0] == first_letter]

    def __repr__(self):
        sorted_products = sorted(self.products, key=lambda x: x)
        result = f"Items in the {self.name} catalogue:\n" + "\n".join(sorted_products)

        return result
