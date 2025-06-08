



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Member_ID": random.randint(1, 1000),
            "Branch_ID": fake.city(),
            "Register_Year": fake.date_time_this_year().strftime("%Y")
        }
        data.append(record)
    return data
