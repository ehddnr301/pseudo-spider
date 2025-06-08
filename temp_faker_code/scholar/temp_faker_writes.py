



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "paperId": random.randint(1, 1000),
            "authorId": random.randint(1, 100)
        }
        data.append(record)
    return data
