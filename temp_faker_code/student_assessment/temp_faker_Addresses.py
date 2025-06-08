


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "address_id": _ + 1,
            "line_1": fake.street_address(),
            "line_2": fake.secondary_address(),
            "city": fake.city(),
            "zip_postcode": fake.zipcode(),
            "state_province_county": fake.state(),
            "country": fake.country()
        }
        data.append(record)
    return data
