



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    fake_data = []
    for _ in range(num_records):
        record = {
            "sid": _ + 1,
            "title": fake.catch_phrase(),
            "release_year": fake.year(),
            "num_of_seasons": random.randint(1, 15),
            "num_of_episodes": random.randint(1, 300),
            "title_aka": fake.catch_phrase(),
            "budget": f"${random.randint(100000, 10000000):,}"
        }
        fake_data.append(record)
    return fake_data
