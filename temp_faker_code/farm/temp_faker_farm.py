



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Farm_ID": _ + 1,
            "Year": fake.date_time_this_year().year,
            "Total_Horses": round(random.uniform(0, 100), 2),
            "Working_Horses": round(random.uniform(0, 100), 2),
            "Total_Cattle": round(random.uniform(0, 100), 2),
            "Oxen": round(random.uniform(0, 100), 2),
            "Bulls": round(random.uniform(0, 100), 2),
            "Cows": round(random.uniform(0, 100), 2),
            "Pigs": round(random.uniform(0, 100), 2),
            "Sheep_and_Goats": round(random.uniform(0, 100), 2)
        }
        data.append(record)
    return data
