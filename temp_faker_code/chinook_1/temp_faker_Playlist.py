


from faker import Faker
import random

def generate_fake_data(num_records):
    fake = Faker()
    data = []
    for _ in range(num_records):
        record = {
            "PlaylistId": random.randint(1, 1000),
            "Name": fake.sentence(nb_words=3)
        }
        data.append(record)
    return data
