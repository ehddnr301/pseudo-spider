



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "County_ID": _ + 1,
            "Name": fake.city(),
            "Population": random.randint(1000, 100000),
            "Police_officers": random.randint(1, 500),
            "Residents_per_officer": random.randint(1, 1000),
            "Case_burden": random.randint(0, 100),
            "Crime_rate": round(random.uniform(0, 10), 2),
            "Police_force": fake.company(),
            "Location": fake.address()
        }
        data.append(record)
    return data
