



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "functional_area_code": fake.bothify(text='??###'),
            "parent_functional_area_code": fake.bothify(text='??###'),
            "functional_area_description": fake.sentence(nb_words=10)
        }
        data.append(record)
    return data
