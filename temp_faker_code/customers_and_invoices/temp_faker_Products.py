


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "product_id": fake.random_int(min=1, max=1000),
            "parent_product_id": fake.random_int(min=1, max=1000),
            "production_type_code": fake.word()[:15],
            "unit_price": round(fake.random_number(digits=5) + fake.random.random(), 4),
            "product_name": fake.word()[:80],
            "product_color": fake.color_name()[:20],
            "product_size": fake.word()[:20]
        }
        data.append(record)
    return data
