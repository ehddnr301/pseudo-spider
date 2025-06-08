



from faker import Faker
import random

def generate_fake_data(num_records):
    fake = Faker()
    data = []
    
    for _ in range(num_records):
        record = {
            "aid": _ + 1,
            "gender": random.choice(["Male", "Female"]),
            "name": fake.name(),
            "nationality": fake.country(),
            "birth_city": fake.city(),
            "birth_year": fake.date_time_this_year().year
        }
        data.append(record)
    
    return data
