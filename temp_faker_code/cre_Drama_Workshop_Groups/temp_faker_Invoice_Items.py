



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Invoice_Item_ID": fake.unique.random_int(min=1, max=10000),
            "Invoice_ID": fake.random_int(min=1, max=10000),
            "Order_ID": fake.random_int(min=1, max=10000),
            "Order_Item_ID": fake.random_int(min=1, max=10000),
            "Product_ID": fake.random_int(min=1, max=10000),
            "Order_Quantity": fake.random_int(min=1, max=100),
            "Other_Item_Details": fake.text(max_nb_chars=255)
        }
        data.append(record)
    return data
