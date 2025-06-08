



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "EMP_NUM": random.randint(1000, 9999),
            "DEPT_CODE": fake.lexify(text='???'),
            "PROF_OFFICE": fake.address(),
            "PROF_EXTENSION": fake.random_int(min=1000, max=9999),
            "PROF_HIGH_DEGREE": fake.random_element(elements=('PhD', 'Masters', 'Bachelors'))
        }
        data.append(record)
    return data
