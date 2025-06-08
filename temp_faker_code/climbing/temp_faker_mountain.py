



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Mountain_ID": _ + 1,
            "Name": fake.word().capitalize(),
            "Height": round(random.uniform(1000, 8848), 2),
            "Prominence": round(random.uniform(100, 3000), 2),
            "Range": fake.word().capitalize(),
            "Country": fake.country()
        }
        data.append(record)
    return data
