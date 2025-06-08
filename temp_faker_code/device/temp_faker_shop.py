


import random
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        shop_id = random.randint(1, 1000)
        shop_name = fake.company()
        location = fake.city()
        open_date = fake.date_time_this_year().strftime("%Y-%m-%d")
        open_year = int(open_date.split("-")[0])
        
        data.append({
            "Shop_ID": shop_id,
            "Shop_Name": shop_name,
            "Location": location,
            "Open_Date": open_date,
            "Open_Year": open_year
        })
    return data
