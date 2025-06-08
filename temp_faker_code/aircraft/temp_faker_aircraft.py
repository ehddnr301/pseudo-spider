


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for i in range(num_records):
        record = {
            "Aircraft_ID": i + 1,
            "Aircraft": fake.word()[:50],
            "Description": fake.sentence()[:50],
            "Max_Gross_Weight": str(random.randint(10000, 50000)),
            "Total_disk_area": str(random.randint(100, 1000)),
            "Max_disk_Loading": str(random.randint(1, 10))
        }
        data.append(record)
    return data
