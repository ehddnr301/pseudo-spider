



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Party_ID": fake.random_int(min=1, max=1000),
            "Event_ID": fake.random_int(min=1, max=1000),
            "Role_Code": fake.random_choices(elements=('Host', 'Guest', 'Speaker'), length=1)[0]
        }
        data.append(record)
    return data
