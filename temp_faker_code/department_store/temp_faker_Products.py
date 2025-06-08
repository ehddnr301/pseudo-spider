


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        product = {
            "product_id": _ + 1,
            "product_type_code": fake.word()[:10],
            "product_name": fake.word()[:80],
            "product_price": round(random.uniform(1.0, 1000.0), 4)
        }
        data.append(product)
    return data
