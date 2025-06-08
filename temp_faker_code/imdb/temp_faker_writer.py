



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "wid": fake.random_int(min=1, max=1000),
            "gender": fake.random_element(elements=("Male", "Female")),
            "name": fake.name(),
            "nationality": fake.random_int(min=1, max=100),
            "num_of_episodes": fake.random_int(min=1, max=100),
            "birth_city": fake.city(),
            "birth_year": fake.year(),
        }
        data.append(record)
    return data
