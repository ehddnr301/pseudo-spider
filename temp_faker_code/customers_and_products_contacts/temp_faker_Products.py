


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "product_id": _ + 1,
            "product_type_code": fake.word()[:15],
            "product_name": fake.catch_phrase()[:80],
            "product_price": round(random.uniform(1.0, 1000.0), 2)
        }
        data.append(record)
    return data
