



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "building_id": fake.uuid4(),
            "Name": fake.company(),
            "Street_address": fake.street_address(),
            "Years_as_tallest": str(random.randint(1, 100)),
            "Height_feet": random.randint(50, 1000),
            "Floors": random.randint(1, 100)
        }
        data.append(record)
    return data
