



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "city_name": fake.city(),
            "population": random.randint(1, 1000000),
            "country_name": fake.country_code(),
            "state_name": fake.state()
        }
        data.append(record)
    return data
