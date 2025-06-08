


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        staff_id = random.randint(1, 1000)
        staff_name = fake.name()
        gender = random.choice(['M', 'F'])
        other_staff_details = fake.text(max_nb_chars=255)
        
        data.append({
            "staff_id": staff_id,
            "staff_name": staff_name,
            "gender": gender,
            "other_staff_details": other_staff_details
        })
    return data
