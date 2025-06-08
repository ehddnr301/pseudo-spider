



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "id": _ + 1,
            "name": fake.name(),
            "Location": fake.city(),
            "Product": fake.word(),
            "Chromosome": fake.word(),
            "OMIM": random.randint(1, 10000),
            "Porphyria": fake.word()
        }
        data.append(record)
    return data
