


import random
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        movie = {
            "movie_id": _ + 1,
            "Title": fake.sentence(nb_words=3),
            "Year": fake.year(),
            "Director": fake.name(),
            "Budget_million": round(random.uniform(1, 200), 2),
            "Gross_worldwide": random.randint(1000000, 300000000)
        }
        data.append(movie)
    return data
