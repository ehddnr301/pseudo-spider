



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "CLASS_CODE": fake.bothify(text='??###'),
            "STU_NUM": random.randint(100000, 999999),
            "ENROLL_GRADE": fake.random_element(elements=('A', 'B', 'C', 'D', 'F'))
        }
        data.append(record)
    return data
