



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "lake_name": fake.name(),
            "area": round(random.uniform(1.0, 10000.0), 2),
            "country_name": fake.country_code(),
            "state_name": fake.state()
        }
        data.append(record)
    return data
