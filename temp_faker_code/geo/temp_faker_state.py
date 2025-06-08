



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        state = {
            "state_name": fake.state(),
            "population": random.randint(100000, 10000000),
            "area": round(random.uniform(5000.0, 500000.0), 2),
            "country_name": fake.country_code(),
            "capital": fake.city(),
            "density": round(random.uniform(10.0, 500.0), 2)
        }
        data.append(state)
    return data
