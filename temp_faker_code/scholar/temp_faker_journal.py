



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for i in range(num_records):
        record = {
            "journalId": i + 1,
            "journalName": fake.catch_phrase()
        }
        data.append(record)
    return data
