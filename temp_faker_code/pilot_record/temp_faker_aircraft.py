



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Aircraft_ID": _ + 1,
            "Order_Year": random.randint(2000, 2023),
            "Manufacturer": fake.company(),
            "Model": fake.word(),
            "Fleet_Series": fake.word(),
            "Powertrain": fake.word(),
            "Fuel_Propulsion": fake.word()
        }
        data.append(record)
    return data
