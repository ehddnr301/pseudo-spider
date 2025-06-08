


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "PetID": _ + 1,
            "PetType": fake.random_element(elements=("Dog", "Cat", "Bird", "Fish", "Reptile")),
            "pet_age": random.randint(1, 15),
            "weight": round(random.uniform(1.0, 30.0), 2)
        }
        data.append(record)
    return data
