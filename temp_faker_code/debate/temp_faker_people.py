



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "People_ID": _ + 1,
            "District": fake.city(),
            "Name": fake.name(),
            "Party": random.choice(['Party A', 'Party B', 'Party C']),
            "Age": random.randint(18, 80)
        }
        data.append(record)
    return data
