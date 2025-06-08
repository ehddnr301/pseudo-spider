



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "department_id": _ + 1,
            "dept_store_id": random.randint(1, 100),
            "department_name": fake.word()[:80]
        }
        data.append(record)
    return data
