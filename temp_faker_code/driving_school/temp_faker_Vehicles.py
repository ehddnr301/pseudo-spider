


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        vehicle_id = random.randint(1, 1000)
        vehicle_details = fake.sentence(nb_words=6)
        data.append({
            "vehicle_id": vehicle_id,
            "vehicle_details": vehicle_details
        })
    return data
