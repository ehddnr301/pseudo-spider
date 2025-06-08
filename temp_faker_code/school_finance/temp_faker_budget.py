



from faker import Faker
import random

fake = Faker()

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        year = fake.date_time_this_year().year
        budgeted = random.randint(1000, 100000)
        invested = random.randint(1000, budgeted)
        total_budget_percent_budgeted = round((budgeted / 100000) * 100, 2)
        total_budget_percent_invested = round((invested / 100000) * 100, 2)
        budget_invested_percent = f"{round((invested / budgeted) * 100, 2)}%"
        
        record = {
            "School_id": fake.unique.random_int(min=1, max=1000),
            "Year": year,
            "Budgeted": budgeted,
            "total_budget_percent_budgeted": total_budget_percent_budgeted,
            "Invested": invested,
            "total_budget_percent_invested": total_budget_percent_invested,
            "Budget_invested_percent": budget_invested_percent
        }
        data.append(record)
    return data
