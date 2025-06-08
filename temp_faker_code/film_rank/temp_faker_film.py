



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Film_ID": _ + 1,
            "Title": fake.catch_phrase(),
            "Studio": fake.company(),
            "Director": fake.name(),
            "Gross_in_dollar": random.randint(100000, 100000000)
        }
        data.append(record)
    return data
