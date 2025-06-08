



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "City_ID": _ + 1,
            "Official_Name": fake.city(),
            "Status": random.choice(["Active", "Inactive"]),
            "Area_km_2": round(random.uniform(10.0, 1000.0), 2),
            "Population": round(random.uniform(1000, 1000000), 2),
            "Census_Ranking": random.choice(["1", "2", "3", "4", "5"])
        }
        data.append(record)
    return data
