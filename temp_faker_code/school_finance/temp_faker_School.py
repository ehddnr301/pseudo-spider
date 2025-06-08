



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "School_id": fake.uuid4(),
            "School_name": fake.company(),
            "Location": fake.city(),
            "Mascot": fake.word(),
            "Enrollment": random.randint(100, 5000),
            "IHSAA_Class": fake.random_element(elements=("1A", "2A", "3A", "4A")),
            "IHSAA_Football_Class": fake.random_element(elements=("1A", "2A", "3A", "4A")),
            "County": fake.county()
        }
        data.append(record)
    return data
