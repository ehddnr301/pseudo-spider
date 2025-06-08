



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "ID": fake.bothify(text='??###'),
            "course_id": fake.bothify(text='???#####'),
            "sec_id": fake.bothify(text='???#####'),
            "semester": fake.random_element(elements=('Fall', 'Spring', 'Summer')),
            "year": fake.year(),
            "grade": fake.random_element(elements=('A', 'B', 'C', 'D', 'F'))
        }
        data.append(record)
    return data
