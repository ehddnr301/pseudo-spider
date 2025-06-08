


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "CountryCode": fake.country_code(),
            "Language": fake.language_name(),
            "IsOfficial": random.choice(['T', 'F']),
            "Percentage": round(random.uniform(0.0, 100.0), 1)
        }
        data.append(record)
    return data
