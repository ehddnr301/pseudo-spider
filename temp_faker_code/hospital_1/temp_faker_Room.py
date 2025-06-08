


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "RoomNumber": fake.random_int(min=1, max=1000),
            "RoomType": fake.random_element(elements=("Single", "Double", "Suite", "Deluxe")),
            "BlockFloor": fake.random_int(min=1, max=10),
            "BlockCode": fake.random_int(min=1, max=5),
            "Unavailable": fake.boolean()
        }
        data.append(record)
    return data
