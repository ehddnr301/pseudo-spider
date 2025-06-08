



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "electoral_register_id": random.randint(1, 10000),
            "cmi_cross_ref_id": random.randint(1, 10000)
        }
        data.append(record)
    return data
