



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "ID": fake.bothify(text='??###'),
            "name": fake.name(),
            "dept_name": fake.word(),
            "salary": round(random.uniform(30000, 120000), 2)
        }
        data.append(record)
    return data
