



from faker import Faker
import random
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        film = {
            "film_id": random.randint(1, 65535),
            "title": fake.sentence(nb_words=6),
            "description": fake.text(),
            "release_year": fake.year(),
            "language_id": random.randint(1, 255),
            "original_language_id": random.choice([None, random.randint(1, 255)]),
            "rental_duration": random.randint(1, 255),
            "rental_rate": round(random.uniform(1.0, 99.99), 2),
            "length": random.choice([None, random.randint(1, 65535)]),
            "replacement_cost": round(random.uniform(1.0, 999.99), 2),
            "rating": random.choice(['G', 'PG', 'PG-13', 'R', 'NC-17']),
            "special_features": None,
            "last_update": fake.date_time_this_year()
        }
        data.append(film)
    return data
