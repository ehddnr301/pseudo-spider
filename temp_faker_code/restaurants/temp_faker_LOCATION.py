


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "RESTAURANT_ID": fake.random_int(min=1, max=1000),
            "HOUSE_NUMBER": fake.random_int(min=1, max=100),
            "STREET_NAME": fake.street_name(),
            "CITY_NAME": fake.city()
        }
        data.append(record)
    return data
