import sys, os
# Add project root to Python path so imports work globally
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from stock.main import process_stock, Product


def test_valid_stock_calculation():
    products: list[Product] = [
        ("p001", 100.0, 2),
        ("p002", 50.0, 3),
    ]
    total, out_of_stock = process_stock(products)
    assert total == 100.0 * 2 + 50.0 * 3
    assert out_of_stock == set()


def test_out_of_stock_detection():
    products: list[Product] = [("p001", 100.0, 0)]
    total, out_of_stock = process_stock(products)
    assert total == 0
    assert "p001" in out_of_stock


def test_string_price_conversion():
    products: list[Product] = [("p001", "99.99", 2)]
    total, out_of_stock = process_stock(products)
    assert total == 99.99 * 2
    assert out_of_stock == set()


def test_negative_quantity():
    products: list[Product] = [("p001", 50.0, -1)]
    total, out_of_stock = process_stock(products)
    assert total == 0
    assert "p001" in out_of_stock


def test_invalid_price():
    products: list[Product] = [("p001", "invalid", 2)]
    total, out_of_stock = process_stock(products)
    assert total == 0
    assert "p001" in out_of_stock
