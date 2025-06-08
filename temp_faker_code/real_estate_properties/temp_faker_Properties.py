



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "property_id": _ + 1,
            "property_type_code": fake.word(),
            "date_on_market": fake.date_time_this_year(),
            "date_sold": fake.date_time_this_year(),
            "property_name": fake.sentence(nb_words=6),
            "property_address": fake.address(),
            "room_count": random.randint(1, 10),
            "vendor_requested_price": round(random.uniform(100000, 1000000), 4),
            "buyer_offered_price": round(random.uniform(100000, 1000000), 4),
            "agreed_selling_price": round(random.uniform(100000, 1000000), 4),
            "apt_feature_1": fake.word(),
            "apt_feature_2": fake.word(),
            "apt_feature_3": fake.word(),
            "fld_feature_1": fake.word(),
            "fld_feature_2": fake.word(),
            "fld_feature_3": fake.word(),
            "hse_feature_1": fake.word(),
            "h
