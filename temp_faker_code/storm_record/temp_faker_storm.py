



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Storm_ID": _ + 1,
            "Name": fake.name(),
            "Dates_active": fake.date_time_this_year().strftime("%Y-%m-%d"),
            "Max_speed": random.randint(50, 200),
            "Damage_millions_USD": round(random.uniform(1.0, 100.0), 2),
            "Number_Deaths": random.randint(0, 500)
        }
        data.append(record)
    return data
