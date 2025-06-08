


import random
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Order_ID": fake.random_int(min=1, max=10000),
            "Customer_ID": fake.random_int(min=1, max=1000),
            "Store_ID": fake.random_int(min=1, max=100),
            "Order_Date": fake.date_time_this_year(),
            "Planned_Delivery_Date": fake.date_time_this_year(),
            "Actual_Delivery_Date": fake.date_time_this_year(),
            "Other_Order_Details": fake.sentence(nb_words=10)
        }
        data.append(record)
    return data
