



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Theme_Park_ID": _ + 1,
            "Theme_Park_Details": fake.catch_phrase()
        }
        data.append(record)
    return data
