



from faker import Faker
import random

def generate_fake_data(num_records):
    fake = Faker()
    data = []
    
    for _ in range(num_records):
        record = {
            "Machine_ID": _ + 1,
            "Making_Year": random.randint(2000, 2023),
            "Class": fake.word(),
            "Team": fake.word(),
            "Machine_series": fake.word(),
            "value_points": round(random.uniform(1.0, 100.0), 2),
            "quality_rank": random.randint(1, 10)
        }
        data.append(record)
    
    return data
