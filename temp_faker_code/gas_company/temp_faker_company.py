



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Company_ID": _ + 1,
            "Rank": random.randint(1, 100),
            "Company": fake.company(),
            "Headquarters": fake.city(),
            "Main_Industry": fake.bs(),
            "Sales_billion": round(random.uniform(1, 100), 2),
            "Profits_billion": round(random.uniform(1, 50), 2),
            "Assets_billion": round(random.uniform(1, 200), 2),
            "Market_Value": round(random.uniform(1, 300), 2)
        }
        data.append(record)
    return data
