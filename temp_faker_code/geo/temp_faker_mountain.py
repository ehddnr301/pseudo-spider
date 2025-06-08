



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "mountain_name": fake.word(),
            "mountain_altitude": random.randint(1000, 8000),
            "country_name": fake.country_code(),
            "state_name": fake.state()
        }
        data.append(record)
    return data
