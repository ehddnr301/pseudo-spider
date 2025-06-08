


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        shop_id = _
        address = fake.address()
        num_of_staff = str(random.randint(1, 100))
        score = round(random.uniform(1, 5), 1)
        open_year = str(fake.date_time_this_year().year)
        
        data.append({
            "Shop_ID": shop_id,
            "Address": address,
            "Num_of_staff": num_of_staff,
            "Score": score,
            "Open_Year": open_year
        })
    return data
