



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "product_id": random.randint(1, 1000),
            "product_name": fake.word(),
            "product_details": fake.sentence()
        }
        data.append(record)
    return data
