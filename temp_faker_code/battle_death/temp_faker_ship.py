



from faker import Faker
import random

def generate_fake_data(num_records):
    fake = Faker()
    data = []
    
    for _ in range(num_records):
        record = {
            "lost_in_battle": random.choice([None, random.randint(0, 1)]),
            "id": fake.unique.random_int(min=1, max=1000),
            "name": fake.name(),
            "tonnage": f"{random.randint(1000, 50000)} tons",
            "ship_type": random.choice(["Cargo", "Battleship", "Cruiser", "Submarine"]),
            "location": fake.city(),
            "disposition_of_ship": random.choice(["Sunk", "Damaged", "In Service", "Scrapped"])
        }
        data.append(record)
    
    return data
