



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "thing_id": fake.random_int(min=1, max=1000),
            "organization_id": fake.random_int(min=1, max=100),
            "Type_of_Thing_Code": fake.lexify(text='?????'),
            "service_type_code": fake.lexify(text='?????'),
            "service_details": fake.sentence(nb_words=10)
        }
        data.append(record)
    return data
