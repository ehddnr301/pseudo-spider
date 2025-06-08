



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    fake_data = []
    for _ in range(num_records):
        record = {
            "Invoice_ID": fake.unique.random_int(min=1, max=10000),
            "Order_ID": fake.unique.random_int(min=1, max=10000),
            "payment_method_code": fake.random_element(elements=('Credit Card', 'PayPal', 'Bank Transfer')),
            "Product_ID": fake.unique.random_int(min=1, max=10000),
            "Order_Quantity": str(fake.random_int(min=1, max=100)),
            "Other_Item_Details": fake.sentence(nb_words=6),
            "Order_Item_ID": fake.unique.random_int(min=1, max=10000)
        }
        fake_data.append(record)
    return fake_data
