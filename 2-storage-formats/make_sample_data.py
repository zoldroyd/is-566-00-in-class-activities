import pandas as pd

rows = []

n_per_country = 50_000

for i in range(1, n_per_country + 1):
    rows.append({
        "order_id": i,
        "customer_id": f"USA_{i:06d}",
        "country": "USA",
        "product": "T-Shirt" if i % 3 == 0 else "Socks",
        "order_date": f"2024-01-{(i % 28) + 1:02d}",
        "sales_amount": (i % 200) + 1
    })

for i in range(n_per_country + 1, 2 * n_per_country + 1):
    rows.append({
        "order_id": i,
        "customer_id": f"UK_{i:06d}",
        "country": "UK",
        "product": "T-Shirt" if i % 3 == 0 else "Socks",
        "order_date": f"2024-01-{(i % 28) + 1:02d}",
        "sales_amount": (i % 200) + 1
    })

df = pd.DataFrame(rows)
df.to_csv("orders_demo.csv", index=False)