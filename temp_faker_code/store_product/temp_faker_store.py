



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Store_ID": _ + 1,
            "Store_Name": fake.company(),
            "Type": random.choice(['Grocery', 'Clothing', 'Electronics', 'Furniture']),
            "Area_size": round(random.uniform(100.0, 10000.0), 2),
            "Number_of_product_category": round(random.uniform(1.0, 50.0), 2),
            "Ranking": random.randint(1, 100)
        }
        data.append(record)
    return data
