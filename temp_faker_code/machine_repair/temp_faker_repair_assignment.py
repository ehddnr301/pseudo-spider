



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "technician_id": random.randint(1, 100),
            "repair_ID": random.randint(1, 1000),
            "Machine_ID": random.randint(1, 500)
        }
        data.append(record)
    return data
