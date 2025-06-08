



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "date": fake.date_time_this_year().strftime("%Y-%m-%d"),
            "max_temperature_f": random.randint(30, 100),
            "mean_temperature_f": random.randint(30, 100),
            "min_temperature_f": random.randint(30, 100),
            "max_dew_point_f": random.randint(30, 100),
            "mean_dew_point_f": random.randint(30, 100),
            "min_dew_point_f": random.randint(30, 100),
            "max_humidity": random.randint(0, 100),
            "mean_humidity": random.randint(0, 100),
            "min_humidity": random.randint(0, 100),
            "max_sea_level_pressure_inches": round(random.uniform(28.0, 32.0), 2),
            "mean_sea_level_pressure_inches": round(random.uniform(28.0, 32.0), 2),
            "min_sea_level_pressure_inches": round(random.uniform(28.0,
