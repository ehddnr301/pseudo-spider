


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "ID": _ + 1,
            "Name": fake.city()[:35],
            "CountryCode": fake.country_code()[:3],
            "District": fake.state()[:20],
            "Population": random.randint(1, 1000000)
        }
        data.append(record)
    return data
