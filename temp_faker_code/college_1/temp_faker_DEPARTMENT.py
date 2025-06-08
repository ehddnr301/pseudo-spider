



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "DEPT_CODE": fake.bothify(text='??###'),
            "DEPT_NAME": fake.catch_phrase(),
            "SCHOOL_CODE": fake.bothify(text='??######'),
            "EMP_NUM": random.randint(1, 1000),
            "DEPT_ADDRESS": fake.street_name(),
            "DEPT_EXTENSION": fake.bothify(text='###')
        }
        data.append(record)
    return data
