



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "School_ID": fake.unique.random_int(min=1, max=1000),
            "Grade": random.choice(['A', 'B', 'C', 'D', 'E']),
            "School": fake.company(),
            "Location": fake.city(),
            "Type": random.choice(['Public', 'Private', 'Charter'])
        }
        data.append(record)
    return data
