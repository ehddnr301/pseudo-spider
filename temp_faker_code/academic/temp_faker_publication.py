



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "abstract": fake.text(),
            "cid": fake.uuid4(),
            "citation_num": random.randint(0, 100),
            "jid": random.randint(1, 1000),
            "pid": _ + 1,
            "reference_num": random.randint(0, 50),
            "title": fake.sentence(),
            "year": fake.date_time_this_year().year
        }
        data.append(record)
    return data
