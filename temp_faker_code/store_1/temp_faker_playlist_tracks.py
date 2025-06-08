


from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "playlist_id": random.randint(1, 1000),
            "track_id": random.randint(1, 1000)
        }
        data.append(record)
    return data
