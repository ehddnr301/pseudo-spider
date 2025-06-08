


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Song_ID": _ + 1,
            "Title": fake.sentence(nb_words=3),
            "Singer_ID": random.randint(1, 100),
            "Sales": round(random.uniform(1000, 100000), 2),
            "Highest_Position": round(random.uniform(1, 100), 2)
        }
        data.append(record)
    return data
