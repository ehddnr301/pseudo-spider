



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "Model_name": fake.word() + " " + fake.word(),
            "Launch_year": random.randint(2000, 2023),
            "RAM_MiB": random.choice([512, 1024, 2048, 4096]),
            "ROM_MiB": random.choice([2048, 4096, 8192, 16384]),
            "Slots": random.choice(["1", "2", "3", "4"]),
            "WiFi": random.choice(["802.11a", "802.11b", "802.11g", "802.11n", "802.11ac"]),
            "Bluetooth": random.choice(["4.0", "4.1", "4.2", "5.0"])
        }
        data.append(record)
    return data
