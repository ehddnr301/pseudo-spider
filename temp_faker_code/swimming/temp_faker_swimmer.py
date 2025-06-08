



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "ID": _ + 1,
            "name": fake.name(),
            "Nationality": fake.country(),
            "meter_100": round(random.uniform(50, 60), 2),
            "meter_200": round(random.uniform(100, 120), 2),
            "meter_300": round(random.uniform(150, 180), 2),
            "meter_400": round(random.uniform(200, 240), 2),
            "meter_500": round(random.uniform(250, 300), 2),
            "meter_600": round(random.uniform(300, 360), 2),
            "meter_700": round(random.uniform(350, 420), 2),
            "Time": fake.date_time_this_year().strftime("%Y-%m-%d %H:%M:%S")
        }
        data.append(record)
    return data
