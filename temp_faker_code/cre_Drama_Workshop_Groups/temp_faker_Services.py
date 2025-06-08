



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Service_ID": _ + 1,
            "Service_Type_Code": fake.lexify(text='?????'),
            "Workshop_Group_ID": random.randint(1, 100),
            "Product_Description": fake.sentence(),
            "Product_Name": fake.word(),
            "Product_Price": round(random.uniform(1.0, 1000.0), 4),
            "Other_Product_Service_Details": fake.sentence()
        }
        data.append(record)
    return data
