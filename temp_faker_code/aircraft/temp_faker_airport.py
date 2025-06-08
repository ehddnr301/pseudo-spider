



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Airport_ID": _ + 1,
            "Airport_Name": fake.city() + " Airport",
            "Total_Passengers": round(random.uniform(1000, 1000000), 2),
            "%_Change_2007": str(round(random.uniform(-10, 10), 2)) + "%",
            "International_Passengers": round(random.uniform(100, 500000), 2),
            "Domestic_Passengers": round(random.uniform(100, 500000), 2),
            "Transit_Passengers": round(random.uniform(0, 100000), 2),
            "Aircraft_Movements": round(random.uniform(100, 10000), 2),
            "Freight_Metric_Tonnes": round(random.uniform(0, 10000), 2)
        }
        data.append(record)
    return data
