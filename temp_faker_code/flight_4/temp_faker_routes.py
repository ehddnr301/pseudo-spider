



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "rid": fake.random_int(min=1, max=1000),
            "dst_apid": fake.random_int(min=1, max=1000),
            "dst_ap": fake.random_uppercase_letter() + fake.random_uppercase_letter() + fake.random_uppercase_letter() + fake.random_uppercase_letter(),
            "src_apid": fake.random_int(min=1, max=100000),
            "src_ap": fake.random_uppercase_letter() + fake.random_uppercase_letter() + fake.random_uppercase_letter() + fake.random_uppercase_letter(),
            "alid": fake.random_int(min=1, max=100000),
            "airline": fake.random_uppercase_letter() + fake.random_uppercase_letter() + fake.random_uppercase_letter() + fake.random_uppercase_letter(),
            "codeshare": fake.text(max_nb_chars=200)
        }
        data.append(record)
    return data
