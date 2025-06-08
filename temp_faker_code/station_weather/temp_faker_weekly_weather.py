



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
    for _ in range(num_records):
        record = {
            "station_id": fake.random_int(min=1, max=100),
            "day_of_week": random.choice(days_of_week),
            "high_temperature": fake.random_int(min=60, max=100),
            "low_temperature": fake.random_int(min=30, max=59),
            "precipitation": round(fake.random_number(digits=2) * 0.01, 2),
            "wind_speed_mph": fake.random_int(min=0, max=20)
        }
        data.append(record)
    
    return data
