


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Book_ID": _ + 1,
            "Title": fake.sentence(nb_words=6),
            "Issues": round(random.uniform(1, 100), 2),
            "Writer": fake.name()
        }
        data.append(record)
    return data
