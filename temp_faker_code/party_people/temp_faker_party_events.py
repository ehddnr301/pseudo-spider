



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Event_ID": _ + 1,
            "Event_Name": fake.catch_phrase(),
            "Party_ID": random.randint(1, 100),
            "Member_in_charge_ID": random.randint(1, 100)
        }
        data.append(record)
    return data
