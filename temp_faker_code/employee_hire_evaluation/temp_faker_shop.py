


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Shop_ID": _ + 1,
            "Name": fake.company(),
            "Location": fake.city(),
            "District": fake.state(),
            "Number_products": random.randint(1, 100),
            "Manager_name": fake.name()
        }
        data.append(record)
    return data
