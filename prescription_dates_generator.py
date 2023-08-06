import random
from datetime import datetime, timedelta


def random_date(start_date, end_date):
    time_delta = end_date - start_date
    random_days = random.randint(0, time_delta.days)
    return start_date + timedelta(days=random_days)


def format_date(date, format):
    return date.strftime(format)


def generate_random_dates():
    # Generate random 'today' within a range of 60 to 365 days from the current date
    current_date = datetime.today()
    today = random_date(
        current_date - timedelta(days=365), current_date - timedelta(days=60)
    )

    # Generate refillEndDate within a range of 7 to 30 days from 'today'
    refill_end_date = random_date(today + timedelta(days=7), today + timedelta(days=30))

    # Generate expiryDate within a range of 30 to 365 days from 'today'
    expiry_date = random_date(today + timedelta(days=30), today + timedelta(days=365))

    # Generate dateFilled within a range of 0 to 7 days from 'today'
    date_filled = random_date(today, today + timedelta(days=7))

    # Define date formats
    formats = [
        "%Y-%m-%d",
        "%m-%d-%Y",
        "%m-%d-%y",
        "%Y-%m-%d",
        "%b %d, %Y",
        "%B %d, %Y",
        "%B %d, %Y",
        "%b %d, %Y",
    ]

    # Convert dates to strings in different formats
    today_str = format_date(today, random.choice(formats))
    refill_end_date_str = format_date(refill_end_date, random.choice(formats))
    expiry_date_str = format_date(expiry_date, random.choice(formats))
    date_filled_str = format_date(date_filled, random.choice(formats))

    return refill_end_date_str, expiry_date_str, date_filled_str


# Test cases
with open("pdg0.txt", "w") as fa:
    with open("pdg1.txt", "w") as fb:
        with open("pdg2.txt", "w") as fc:
            for _ in range(1000):
                a, b, c = generate_random_dates()
                fa.write(f"{a}\n")
                fb.write(f"{b}\n")
                fc.write(f"{c}\n")
