



from faker import Faker
import random

def generate_fake_data(num_records):
    fake = Faker()
    data = []
    
    for _ in range(num_records):
        record = {
            "Wrestler_ID": _ + 1,
            "Name": fake.name(),
            "Reign": fake.word(),
            "Days_held": str(random.randint(1, 365)),
            "Location": fake.city(),
            "Event": fake.word()
        }
        data.append(record)
    
    return data
