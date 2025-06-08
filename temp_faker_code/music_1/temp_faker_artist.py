



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "artist_name": fake.name(),
            "country": fake.country(),
            "gender": random.choice(["Male", "Female"]),
            "preferred_genre": fake.word()
        }
        data.append(record)
    return data
