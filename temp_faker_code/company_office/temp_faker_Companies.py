



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "id": _ + 1,
            "name": fake.company(),
            "Headquarters": fake.city(),
            "Industry": fake.bs(),
            "Sales_billion": round(random.uniform(1, 100), 2),
            "Profits_billion": round(random.uniform(1, 50), 2),
            "Assets_billion": round(random.uniform(1, 200), 2),
            "Market_Value_billion": str(round(random.uniform(1, 300), 2))
        }
        data.append(record)
    return data
