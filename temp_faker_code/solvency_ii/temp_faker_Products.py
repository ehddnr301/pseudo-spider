



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Product_ID": _ + 1,
            "Product_Type_Code": fake.lexify(text='?????'),
            "Product_Name": fake.word() + " " + fake.word(),
            "Product_Price": round(random.uniform(1, 1000), 4)
        }
        data.append(record)
    return data
