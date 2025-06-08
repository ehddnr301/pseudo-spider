


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        lettergrade = fake.random_element(elements=('A', 'B', 'C', 'D', 'F'))
        gradepoint = round(random.uniform(0.0, 4.0), 2)
        data.append({
            'lettergrade': lettergrade,
            'gradepoint': gradepoint
        })
    return data
