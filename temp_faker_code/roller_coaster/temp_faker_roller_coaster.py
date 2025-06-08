



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Roller_Coaster_ID": _ + 1,
            "Name": fake.catch_phrase(),
            "Park": fake.company(),
            "Country_ID": random.randint(1, 100),
            "Length": round(random.uniform(100, 3000), 2),
            "Height": round(random.uniform(10, 200), 2),
            "Speed": f"{random.randint(30, 100)} km/h",
            "Opened": fake.date_time_this_year().strftime("%Y-%m-%d"),
            "Status": random.choice(["Operating", "Closed", "Under Maintenance"])
        }
        data.append(record)
    return data
