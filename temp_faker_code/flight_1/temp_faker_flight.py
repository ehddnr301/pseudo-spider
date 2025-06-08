



from faker import Faker
import random

def generate_fake_data(num_records):
    fake = Faker()
    data = []
    
    for _ in range(num_records):
        record = {
            "flno": random.randint(1000, 9999),
            "origin": fake.city(),
            "destination": fake.city(),
            "distance": random.randint(100, 999999),
            "departure_date": fake.date_time_this_year(),
            "arrival_date": fake.date_time_this_year(),
            "price": round(random.uniform(100, 9999), 2),
            "aid": random.randint(100000000, 999999999)
        }
        data.append(record)
    
    return data
