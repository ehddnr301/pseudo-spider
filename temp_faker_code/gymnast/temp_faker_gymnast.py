


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        gymnast = {
            "Gymnast_ID": _ + 1,
            "Floor_Exercise_Points": round(random.uniform(0, 10), 2),
            "Pommel_Horse_Points": round(random.uniform(0, 10), 2),
            "Rings_Points": round(random.uniform(0, 10), 2),
            "Vault_Points": round(random.uniform(0, 10), 2),
            "Parallel_Bars_Points": round(random.uniform(0, 10), 2),
            "Horizontal_Bar_Points": round(random.uniform(0, 10), 2),
            "Total_Points": round(random.uniform(0, 70), 2)
        }
        data.append(gymnast)
    return data


import random
from faker import Faker

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        gymnast = {
            "Gymnast_ID": _ + 1,
            "Floor_Exercise_Points": round(random.uniform
