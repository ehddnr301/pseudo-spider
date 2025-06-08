


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "product_category_code": fake.unique.lexify(text='?????'),
            "product_category_description": fake.sentence(nb_words=6),
            "unit_of_measure": fake.random_element(elements=('kg', 'g', 'lb', 'oz', 'l')),
        }
        data.append(record)
    return data
