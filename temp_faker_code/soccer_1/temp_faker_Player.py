



from faker import Faker
import random

def generate_fake_data(num_records):
    fake = Faker()
    data = []
    
    for _ in range(num_records):
        record = {
            "id": _ + 1,
            "player_api_id": random.randint(1, 10000),
            "player_name": fake.name(),
            "player_fifa_api_id": random.randint(1, 10000),
            "birthday": fake.date_time_this_year().strftime('%Y-%m-%d'),
            "height": random.randint(150, 200),
            "weight": random.randint(50, 100)
        }
        data.append(record)
    
    return data
