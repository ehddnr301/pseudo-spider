



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "raceId": random.randint(1, 100),
            "driverId": random.randint(1, 50),
            "stop": random.randint(1, 5),
            "lap": random.randint(1, 70),
            "time": fake.date_time_this_year().strftime("%H:%M:%S"),
            "duration": f"{random.randint(1, 10)}.{random.randint(0, 999)}",
            "milliseconds": random.randint(1000, 300000)
        }
        data.append(record)
    return data
