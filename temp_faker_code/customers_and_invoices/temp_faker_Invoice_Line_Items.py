


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "order_item_id": random.randint(1, 1000),
            "invoice_number": random.randint(1000, 9999),
            "product_id": random.randint(1, 1000),
            "product_title": fake.catch_phrase(),
            "product_quantity": str(random.randint(1, 100)),
            "product_price": round(random.uniform(1.0, 1000.0), 4),
            "derived_product_cost": round(random.uniform(1.0, 1000.0), 4),
            "derived_vat_payable": round(random.uniform(0.0, 200.0), 4),
            "derived_total_cost": round(random.uniform(1.0, 1200.0), 4)
        }
        data.append(record)
    return data
