


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "TrackId": _ + 1,
            "Name": fake.sentence(nb_words=3),
            "AlbumId": random.randint(1, 100),
            "MediaTypeId": random.randint(1, 5),
            "GenreId": random.randint(1, 10),
            "Composer": fake.name(),
            "Milliseconds": random.randint(100000, 300000),
            "Bytes": random.randint(1000, 1000000),
            "UnitPrice": round(random.uniform(0.99, 9.99), 2)
        }
        data.append(record)
    return data
