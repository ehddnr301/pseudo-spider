



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Artwork_ID": _ + 1,
            "Type": fake.word(),
            "Name": fake.catch_phrase()
        }
        data.append(record)
    return data
