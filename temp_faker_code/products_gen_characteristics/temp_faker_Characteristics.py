


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "characteristic_id": _ + 1,
            "characteristic_type_code": fake.word()[:15],
            "characteristic_data_type": fake.word()[:10],
            "characteristic_name": fake.sentence(nb_words=3)[:-1],
            "other_characteristic_details": fake.text(max_nb_chars=255)
        }
        data.append(record)
    return data
