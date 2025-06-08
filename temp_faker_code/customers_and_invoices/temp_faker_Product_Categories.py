


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "production_type_code": fake.lexify(text='?????'),
            "product_type_description": fake.sentence(nb_words=6),
            "vat_rating": round(random.uniform(0, 1), 4)
        }
        data.append(record)
    return data
