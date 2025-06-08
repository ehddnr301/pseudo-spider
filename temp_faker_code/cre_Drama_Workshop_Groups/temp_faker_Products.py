



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Product_ID": fake.uuid4(),
            "Product_Name": fake.word(),
            "Product_Price": round(random.uniform(1, 1000), 4),
            "Product_Description": fake.sentence(),
            "Other_Product_Service_Details": fake.sentence()
        }
        data.append(record)
    return data
