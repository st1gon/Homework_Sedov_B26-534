import random
from datetime import datetime, timedelta


def generate_sales_file(filename="sales_data.csv", num_rows=5000):
    products = ["Book", "Pen", "Notebook", "Laptop", "Mouse", "Keyboard"]
    start_date = datetime(2026, 1, 1)

    with open(filename, "w", encoding="utf-8") as f:
        f.write("date,product,quantity,price\n")
        for _ in range(num_rows):
            if random.random() < 0.02:
                f.write("INVALID_DATA_FORMAT\n")
                continue

            date_str = (start_date + timedelta(days=random.randint(0, 90))).strftime("%Y-%m-%d")
            product = random.choice(products)
            qty = random.randint(1, 15)
            price = random.randint(50, 50000)
            f.write(f"{date_str},{product},{qty},{price}\n")


def analyze_sales(filename="sales_data.csv"):
    total_sales_amount = 0
    product_quantities = {}
    product_revenue = {}
    daily_revenue = {}
    valid_transactions = 0

    with open(filename, "r", encoding="utf-8") as f:
        _ = f.readline()
        for line in f:
            parts = line.strip().split(",")
            if len(parts) != 4:
                continue
            date, product, qty_str, price_str = parts
            try:
                qty = int(qty_str)
                price = float(price_str)
            except ValueError:
                continue

            revenue = qty * price
            total_sales_amount += revenue
            valid_transactions += 1

            product_quantities[product] = product_quantities.get(product, 0) + qty
            product_revenue[product] = product_revenue.get(product, 0) + revenue
            daily_revenue[date] = daily_revenue.get(date, 0) + revenue

    if valid_transactions == 0:
        print("Нет корректных данных для анализа.")
        return

    best_qty_product = max(product_quantities, key=product_quantities.get)
    best_rev_product = max(product_revenue, key=product_revenue.get)
    best_day = max(daily_revenue, key=daily_revenue.get)
    avg_purchase_cost = total_sales_amount / valid_transactions

    print(f"Общая сумма продаж: {total_sales_amount:.2f}")
    print(f"Самый продаваемый товар по количеству: {best_qty_product}")
    print(f"Товар с максимальной выручкой: {best_rev_product}")
    print(f"Средняя стоимость одной покупки: {avg_purchase_cost:.2f}")
    print(f"День с максимальной выручкой: {best_day}")


if __name__ == "__main__":
    generate_sales_file()
    analyze_sales()
