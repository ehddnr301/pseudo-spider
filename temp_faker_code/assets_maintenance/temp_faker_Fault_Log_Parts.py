


from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "fault_log_entry_id": fake.random_int(min=1, max=1000),
            "part_fault_id": fake.random_int(min=1, max=1000),
            "fault_status": fake.random_element(elements=("active", "inactive", "pending")),
        }
        data.append(record)
    return data
