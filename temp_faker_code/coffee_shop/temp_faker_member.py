


import random
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Member_ID": _ + 1,
            "Name": fake.name(),
            "Membership_card": fake.uuid4(),
            "Age": random.randint(18, 70),
            "Time_of_purchase": int(fake.date_time_this_year().timestamp()),
            "Level_of_membership": random.randint(1, 5),
            "Address": fake.address().replace("\n", ", ")
        }
        data.append(record)
    return data
