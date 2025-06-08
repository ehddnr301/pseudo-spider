



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "song_name": fake.sentence(nb_words=3)[:-1],
            "artist_name": fake.name(),
            "country": fake.country(),
            "f_id": random.randint(1, 10000),
            "genre_is": fake.word(),
            "rating": random.randint(1, 10),
            "languages": fake.language_name(),
            "releasedate": fake.date_time_this_year(),
            "resolution": random.randint(1, 1000)
        }
        data.append(record)
    return data
