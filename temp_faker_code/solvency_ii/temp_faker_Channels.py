



from faker import Faker
import random

def generate_fake_data(num_records):
    fake = Faker()
    data = []
    for _ in range(num_records):
        record = {
            "Channel_ID": random.randint(1, 1000),
            "Other_Details": fake.sentence(nb_words=6)
        }
        data.append(record)
    return data
