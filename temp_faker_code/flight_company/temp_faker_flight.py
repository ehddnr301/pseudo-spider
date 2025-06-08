



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "id": _ + 1,
            "Vehicle_Flight_number": fake.bothify(text='??###'),
            "Date": fake.date_time_this_year().isoformat(),
            "Pilot": fake.name(),
            "Velocity": round(random.uniform(200.0, 900.0), 2),
            "Altitude": round(random.uniform(1000.0, 35000.0), 2),
            "airport_id": random.randint(1, 100),
            "company_id": random.randint(1, 50)
        }
        data.append(record)
    return data
