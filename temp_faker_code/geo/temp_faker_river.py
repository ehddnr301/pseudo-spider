



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "river_name": fake.name(),
            "length": random.randint(1, 10000),
            "country_name": fake.country_code(),
            "traverse": fake.text(max_nb_chars=200)
        }
        data.append(record)
    return data
