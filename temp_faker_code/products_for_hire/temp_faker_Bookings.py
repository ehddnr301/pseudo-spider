



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    fake_data = []
    for _ in range(num_records):
        record = {
            "booking_id": _ + 1,
            "customer_id": random.randint(1, 1000),
            "booking_status_code": fake.random_element(elements=("CONFIRMED", "CANCELLED", "PENDING")),
            "returned_damaged_yn": fake.random_element(elements=("Y", "N")),
            "booking_start_date": fake.date_time_this_year(),
            "booking_end_date": fake.date_time_this_year(),
            "count_hired": str(random.randint(1, 10)),
            "amount_payable": round(random.uniform(10.0, 1000.0), 4),
            "amount_of_discount": round(random.uniform(0.0, 100.0), 4),
            "amount_outstanding": round(random.uniform(0.0, 1000.0), 4),
            "amount_of_refund": round(random.uniform(0.0, 500.0), 4)
        }
        fake_data.append(record)
    return fake_data
