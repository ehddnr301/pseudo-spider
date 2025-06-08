



from faker import Faker
import random

def generate_fake_data(num_records):
    fake = Faker()
    data = []
    
    for _ in range(num_records):
        record = {
            "part_fault_id": _ + 1,
            "part_id": random.randint(1, 100),
            "fault_short_name": fake.word()[:20],
            "fault_description": fake.sentence()[:255],
            "other_fault_details": fake.sentence()[:255]
        }
        data.append(record)
    
    return data
