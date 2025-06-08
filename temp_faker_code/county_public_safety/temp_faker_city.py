



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "City_ID": _ + 1,
            "County_ID": random.randint(1, 100),
            "Name": fake.city(),
            "White": round(random.uniform(0, 1), 2),
            "Black": round(random.uniform(0, 1), 2),
            "Amerindian": round(random.uniform(0, 1), 2),
            "Asian": round(random.uniform(0, 1), 2),
            "Multiracial": round(random.uniform(0, 1), 2),
            "Hispanic": round(random.uniform(0, 1), 2)
        }
        data.append(record)
    return data
