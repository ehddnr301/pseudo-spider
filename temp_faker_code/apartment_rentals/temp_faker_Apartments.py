



from faker import Faker
import random

def generate_fake_data(num_records):
    fake = Faker()
    data = []
    
    for _ in range(num_records):
        record = {
            "apt_id": _ + 1,
            "building_id": random.randint(1, 100),
            "apt_type_code": fake.word()[:15],
            "apt_number": fake.building_number()[:10],
            "bathroom_count": random.randint(1, 5),
            "bedroom_count": random.randint(1, 5),
            "room_count": str(random.randint(1, 5))
        }
        data.append(record)
    
    return data
