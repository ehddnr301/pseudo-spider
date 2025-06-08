


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "charge_id": _ + 1,
            "charge_type": fake.random_element(elements=("type1", "type2", "type3")),
            "charge_amount": round(random.uniform(1.0, 1000.0), 4)
        }
        data.append(record)
    return data
