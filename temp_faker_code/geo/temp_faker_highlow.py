



from faker import Faker
import random

def generate_fake_data(num_records):
    fake = Faker()
    data = []
    
    for _ in range(num_records):
        record = {
            "state_name": fake.state(),
            "highest_elevation": str(random.randint(1000, 15000)) + " ft",
            "lowest_point": str(random.randint(-500, 0)) + " ft",
            "highest_point": str(random.randint(1000, 15000)) + " ft",
            "lowest_elevation": str(random.randint(-500, 0)) + " ft"
        }
        data.append(record)
    
    return data
