from faker import Faker
import random

fake = Faker()


def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Code": fake.unique.random_uppercase_letter()
            + fake.unique.random_uppercase_letter()
            + fake.unique.random_uppercase_letter(),
            "Name": fake.country(),
            "Continent": fake.random_element(
                elements=(
                    "Asia",
                    "Europe",
                    "Africa",
                    "Oceania",
                    "North America",
                    "South America",
                )
            ),
            "Region": fake.word(),
            "SurfaceArea": round(random.uniform(0.01, 10000.00), 2),
            "IndepYear": fake.year(),
            "Population": fake.random_int(min=1, max=1000000000),
            "LifeExpectancy": round(random.uniform(1.0, 100.0), 1),
            "GNP": round(random.uniform(0.01, 1000000.00), 2),
            "GNPOld": round(random.uniform(0.01, 1000000.00), 2),
            "LocalName": fake.city(),
            "GovernmentForm": fake.word(),
            "HeadOfState": fake.name(),
            "Capital": fake.random_int(min=1, max=1000000000),
            "Code2": fake.unique.random_uppercase_letter()
            + fake.unique.random_uppercase_letter(),
        }
        data.append(record)
    return data
