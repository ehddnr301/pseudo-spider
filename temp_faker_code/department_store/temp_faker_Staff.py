


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        staff_id = _
        staff_gender = random.choice(['M', 'F'])
        staff_name = fake.name()
        
        data.append({
            "staff_id": staff_id,
            "staff_gender": staff_gender,
            "staff_name": staff_name
        })
    return data
