



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "id": _ + 1,
            "name": fake.sentence(nb_words=3),
            "album_id": random.choice([None, random.randint(1, 100)]),
            "media_type_id": random.randint(1, 5),
            "genre_id": random.choice([None, random.randint(1, 10)]),
            "composer": fake.name(),
            "milliseconds": random.randint(100000, 300000),
            "bytes": random.choice([None, random.randint(1000, 1000000)]),
            "unit_price": round(random.uniform(0.99, 9.99), 2)
        }
        data.append(record)
    return data
