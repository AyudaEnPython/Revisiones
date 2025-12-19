"""AyudaEnPython: https://www.facebook.com/groups/ayudapython"""

from abc import ABC, abstractmethod
from datetime import datetime
from typing import List, Optional, Protocol


class HasNameAndSKU(Protocol):
    name: str
    sku: str


def print_name_and_sku(entity: HasNameAndSKU, label) -> None:
    print(f"\n{label} INFO: {entity.name} (SKU: {entity.sku})")


class ProductDetail(ABC):
    @abstractmethod
    def apply_pricing(self, base_price: float) -> float: ...

    @abstractmethod
    def extra_info(self) -> str: ...

    def fulfill(self) -> None: ...


class Product:
    TAX_RATE: float = 0.18

    def __init__(
        self,
        sku: str,
        name: str,
        price: float,
        detail: Optional[ProductDetail] = None,
    ) -> None:
        self.sku = sku
        self.name = name
        self.price = price
        self.detail = detail

    def final_price(self) -> float:
        base = self.price * (1 + self.TAX_RATE)
        return self.detail.apply_pricing(base) if self.detail else base

    def info(self) -> str:
        info = f"SKU: {self.sku} - {self.name} (Base Price: ${self.price:.2f})"
        if self.detail:
            info += self.detail.extra_info()
        return info


class ShippingDetail(ProductDetail):
    def __init__(
        self, weight_kg: float, dimensions: str, cost_per_kg: float = 2.5
    ) -> None:
        self.weight_kg = weight_kg
        self.dimensions = dimensions
        self.cost_per_kg = cost_per_kg

    def apply_pricing(self, base_price: float) -> float:
        return base_price + self.shipping_cost()

    def shipping_cost(self) -> float:
        return self.weight_kg * self.cost_per_kg

    def extra_info(self) -> str:
        return (
            f"\n\tWeight: {self.weight_kg}kg"
            f"\n\tDimensions: {self.dimensions}"
            f"\n\tShipping: ${self.shipping_cost():.2f}"
        )


class DigitalDetail(ProductDetail):
    def __init__(self, download_url: str, file_format: str = "MP4") -> None:
        self.download_url = download_url
        self.file_format = file_format

    def apply_pricing(self, base_price: float) -> float:
        return base_price

    def extra_info(self) -> str:
        return f"\n\tFormat: {self.file_format}\n\tURL: {self.download_url}"

    def fulfill(self) -> None:
        print(f"Sending download link for '{self.download_url}'...")


class SubscriptionDetail(ProductDetail):
    def __init__(self, duration_months: int) -> None:
        self.duration_months = duration_months
        self.activation_date = datetime.now().date()

    def apply_pricing(self, base_price: float) -> float:
        return base_price * self.duration_months

    def extra_info(self) -> str:
        return (
            f"\n\tDuration: {self.duration_months} month(s)"
            f"\n\tActivation: {self.activation_date}"
        )

    def fulfill(self) -> None:
        print("Checking status of subscription. Active.")


class Employee:
    def __init__(self, name: str, employee_id: str) -> None:
        self.name = name
        self.sku = employee_id


class Cart:
    def __init__(self, products: Optional[List[Product]] = None) -> None:
        self._products = products or []

    def add(self, product: Product) -> None:
        self._products.append(product)

    def items(self) -> List[Product]:
        return list(self._products)

    def total(self) -> float:
        return sum(product.final_price() for product in self._products)


class CheckoutService:
    @staticmethod
    def fulfill(cart: Cart) -> None:
        print("\n------- FULFILLING CART ------")
        for product in cart.items():
            if product.detail:
                product.detail.fulfill()


class CartPrinter:
    @staticmethod
    def print_summary(cart: Cart) -> None:
        print("\n-------- CART SUMMARY --------")
        for product in cart.items():
            print(product.info())

    @staticmethod
    def print_detailed_total(cart: Cart) -> None:
        print("\n--------- CART TOTAL ---------")
        for product in cart.items():
            print(f"{product.name:>22}: ${product.final_price():.2f}")
        print("------------------------------")
        print(f"${cart.total():>29.2f}")


if __name__ == "__main__":
    shopping_cart = [
        Product(
            "LIB-001",
            "Python Pro",
            45.00,
            detail=ShippingDetail(weight_kg=0.8, dimensions="20x15x3 cm"),
        ),
        Product(
            "SERV-ANTV",
            "Antivirus Total 1 Year",
            5.00,
            detail=SubscriptionDetail(duration_months=12),
        ),
        Product(
            "DIG-CRS-003",
            "Advanced OOP Course",
            75.00,
            detail=DigitalDetail(
                download_url="https://learn.ayudaenpython.com"
            ),
        ),
    ]
    cart = Cart(shopping_cart)
    CartPrinter.print_summary(cart)
    CartPrinter.print_detailed_total(cart)
    CheckoutService.fulfill(cart)

    employee = Employee("Juan Perez", "EMP-001")
    print_name_and_sku(employee, "EMPLOYEE")