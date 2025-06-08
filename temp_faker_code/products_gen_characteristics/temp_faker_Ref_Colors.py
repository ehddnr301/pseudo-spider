



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        color_code = fake.hex_color()[1:]  # Remove the '#' character
        color_description = fake.color_name()
        data.append({
            "color_code": color_code,
            "color_description": color_description
        })
    return data
