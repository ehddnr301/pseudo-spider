



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Company_ID": random.uniform(1, 1000),
            "Name": fake.company(),
            "Headquarters": fake.city(),
            "Industry": fake.bs(),
            "Sales_in_Billion": round(random.uniform(1, 100), 2),
            "Profits_in_Billion": round(random.uniform(1, 50), 2),
            "Assets_in_Billion": round(random.uniform(1, 200), 2),
            "Market_Value_in_Billion": round(random.uniform(1, 300), 2)
        }
        data.append(record)
    return data
