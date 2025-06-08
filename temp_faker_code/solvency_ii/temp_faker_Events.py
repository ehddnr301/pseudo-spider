



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Event_ID": _ + 1,
            "Address_ID": random.randint(1, 100),
            "Channel_ID": random.randint(1, 10),
            "Event_Type_Code": fake.word()[:15],
            "Finance_ID": random.randint(1, 1000),
            "Location_ID": random.randint(1, 500)
        }
        data.append(record)
    return data
