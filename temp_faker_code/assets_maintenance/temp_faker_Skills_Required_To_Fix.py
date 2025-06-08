



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "part_fault_id": random.randint(1, 100),
            "skill_id": random.randint(1, 100)
        }
        data.append(record)
    return data
