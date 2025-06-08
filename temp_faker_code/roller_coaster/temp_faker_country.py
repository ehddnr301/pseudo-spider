



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Country_ID": _ + 1,
            "Name": fake.country(),
            "Population": random.randint(100000, 100000000),
            "Area": random.randint(1000, 1000000),
            "Languages": fake.language_name()
        }
        data.append(record)
    return data
