"""
Stock Management Module
=======================

This module provides functionality for processing product stock data,
calculating total stock value, and identifying out-of-stock products.

Example:
--------
products = [
    ("p001", 150.00, 5),
    ("p002", 200.00, 0),
    ("p003", 50.50, 10),
    ("p004", "99.99", 3),
    ("p005", 300.00, 0),
    ("p006", 75.00, -1),
]

total, out_of_stock = process_stock(products)
print(total)
print(out_of_stock)
"""

from typing import List, Tuple, Union, Set


# Type alias for product tuple
Product = Tuple[str, Union[float, str], int]


def process_stock(product_list: List[Product]) -> Tuple[float, Set[str]]:
    """
    Process a list of products and calculate total stock value and out-of-stock items.

    Args:
        product_list (List[Product]): List of products as (product_id, price, quantity).

    Returns:
        Tuple[float, Set[str]]:
            - Total value of all valid stock.
            - Set of product IDs that are out of stock or invalid.
    """
    total_value: float = 0.0
    out_of_stock_items: Set[str] = set()

    for product_id, price, quantity in product_list:
        try:
            # Convert price to float if it's a string
            price_value = float(price)

            # Ignore negative quantities
            if quantity < 0:
                out_of_stock_items.add(product_id)
                continue

            stock_value = price_value * quantity

            # If no stock, mark as out of stock
            if quantity == 0:
                out_of_stock_items.add(product_id)

            total_value += stock_value

        except (ValueError, TypeError):
            # Invalid price or data type, treat as out of stock
            out_of_stock_items.add(product_id)

    return total_value, out_of_stock_items


if __name__ == "__main__":
    products: List[Product] = [
        ("p001", 150.00, 5),
        ("p002", 200.00, 0),
        ("p003", 50.50, 10),
        ("p004", "99.99", 3),
        ("p005", 300.00, 0),
        ("p006", 75.00, -1),
    ]

    total_value, low_stock = process_stock(products)
    print(f"Total value of all stock: {total_value}")
    print(f"Out of stock products: {low_stock}")
