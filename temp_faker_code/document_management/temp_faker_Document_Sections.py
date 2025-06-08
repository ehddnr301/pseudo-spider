



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "section_id": _ + 1,
            "document_code": fake.bothify(text='??###'),
            "section_sequence": random.randint(1, 100),
            "section_code": fake.bothify(text='??-###'),
            "section_title": fake.sentence(nb_words=6)
        }
        data.append(record)
    return data
