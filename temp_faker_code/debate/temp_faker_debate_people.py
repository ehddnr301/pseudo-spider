



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Debate_ID": fake.random_int(min=1, max=1000),
            "Affirmative": fake.random_int(min=1, max=100),
            "Negative": fake.random_int(min=1, max=100),
            "If_Affirmative_Win": fake.boolean()
        }
        data.append(record)
    return data
