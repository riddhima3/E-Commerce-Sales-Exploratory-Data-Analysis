import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

np.random.seed(42)
random.seed(42)

n = 5000

categories = ['Electronics', 'Clothing', 'Home & Kitchen', 'Books', 'Sports', 'Beauty']
cat_weights = [0.25, 0.20, 0.20, 0.10, 0.15, 0.10]

products = {
    'Electronics': ['Laptop', 'Smartphone', 'Headphones', 'Tablet', 'Smartwatch'],
    'Clothing':    ['T-Shirt', 'Jeans', 'Dress', 'Jacket', 'Sneakers'],
    'Home & Kitchen': ['Blender', 'Coffee Maker', 'Cookware Set', 'Air Fryer', 'Toaster'],
    'Books':       ['Fiction Novel', 'Self-Help Book', 'Textbook', 'Cookbook', 'Biography'],
    'Sports':      ['Yoga Mat', 'Dumbbells', 'Running Shoes', 'Cycle Helmet', 'Jump Rope'],
    'Beauty':      ['Face Cream', 'Lipstick', 'Shampoo', 'Perfume', 'Sunscreen']
}

price_ranges = {
    'Electronics': (199, 1499),
    'Clothing': (19, 149),
    'Home & Kitchen': (29, 249),
    'Books': (9, 49),
    'Sports': (15, 199),
    'Beauty': (10, 89)
}

cities = ['Mumbai', 'Delhi', 'Bangalore', 'Hyderabad', 'Chennai', 'Kolkata', 'Pune', 'Ahmedabad']
payment_methods = ['Credit Card', 'Debit Card', 'UPI', 'Net Banking', 'Cash on Delivery']
payment_weights = [0.30, 0.20, 0.30, 0.10, 0.10]

start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)

rows = []
for i in range(n):
    cat = np.random.choice(categories, p=cat_weights)
    product = random.choice(products[cat])
    lo, hi = price_ranges[cat]
    price = round(random.uniform(lo, hi), 2)
    qty = random.choices([1,2,3,4,5], weights=[0.5,0.25,0.12,0.08,0.05])[0]
    discount = random.choices([0, 0.05, 0.10, 0.15, 0.20], weights=[0.4,0.2,0.2,0.1,0.1])[0]
    revenue = round(price * qty * (1 - discount), 2)
    order_date = start_date + timedelta(days=random.randint(0, 364))
    city = random.choice(cities)
    payment = np.random.choice(payment_methods, p=payment_weights)
    rating = round(random.uniform(2.5, 5.0), 1)
    returned = random.choices([0, 1], weights=[0.88, 0.12])[0]

    rows.append({
        'order_id': f'ORD{10000+i}',
        'order_date': order_date.strftime('%Y-%m-%d'),
        'category': cat,
        'product': product,
        'unit_price': price,
        'quantity': qty,
        'discount': discount,
        'revenue': revenue,
        'city': city,
        'payment_method': payment,
        'rating': rating,
        'returned': returned
    })

df = pd.DataFrame(rows)
df.to_csv('data/ecommerce_sales.csv', index=False)
print(f"Dataset saved: {len(df)} rows")
print(df.head())
