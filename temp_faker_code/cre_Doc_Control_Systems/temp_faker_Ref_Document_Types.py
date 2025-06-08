



from faker import Faker
import random

def generate_fake_data(num_records):
    fake = Faker()
    data = []
    for _ in range(num_records):
        record = {
            "document_type_code": fake.bothify(text='??##############'),  # CHAR(15)
            "document_type_description": fake.sentence(nb_words=10)  # VARCHAR(255)
        }
        data.append(record)
    return data
