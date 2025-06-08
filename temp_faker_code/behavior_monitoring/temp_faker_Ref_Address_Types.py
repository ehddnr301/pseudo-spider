



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "address_type_code": fake.lexify(text='???'),
            "address_type_description": fake.sentence(nb_words=6)
        }
        data.append(record)
    return data
