



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "id": _ + 1,
            "name": fake.name(),
            "Operating_system": random.choice(['Windows', 'macOS', 'Linux']),
            "Client": random.choice(['Chrome', 'Firefox', 'Safari', 'Edge']),
            "Connection": random.choice(['WiFi', 'Ethernet', 'Mobile'])
        }
        data.append(record)
    return data
