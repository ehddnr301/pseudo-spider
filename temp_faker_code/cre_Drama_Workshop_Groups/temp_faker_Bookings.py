



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Booking_ID": _ + 1,
            "Customer_ID": random.randint(1, 1000),
            "Workshop_Group_ID": fake.word(),
            "Status_Code": fake.lexify(text='?????'),
            "Store_ID": random.randint(1, 100),
            "Order_Date": fake.date_time_this_year(),
            "Planned_Delivery_Date": fake.date_time_this_year(),
            "Actual_Delivery_Date": fake.date_time_this_year(),
            "Other_Order_Details": fake.sentence() 
        }
        data.append(record)
    return data
