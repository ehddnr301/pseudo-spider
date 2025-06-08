



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "mID": _ + 1,
            "title": fake.sentence(nb_words=3),
            "year": random.randint(1900, 2023),
            "director": fake.name()
        }
        data.append(record)
    return data
