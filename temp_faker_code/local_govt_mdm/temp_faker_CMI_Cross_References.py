



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "cmi_cross_ref_id": fake.unique.random_int(min=1, max=10000),
            "master_customer_id": fake.random_int(min=1, max=10000),
            "source_system_code": fake.lexify(text='?????')[:15]
        }
        data.append(record)
    return data
