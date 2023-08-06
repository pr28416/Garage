import random
import requests


def fetch_us_cities():
    # Fetch a list of US cities using the "SimpleMaps" API
    response = requests.get(
        "https://simplemaps.com/static/data/us-cities/uscitiesv1.6.json"
    )
    data = response.json()
    return [city["city"] for city in data]


def fetch_us_states():
    # List of US state abbreviations
    return [
        "AL",
        "AK",
        "AZ",
        "AR",
        "CA",
        "CO",
        "CT",
        "DE",
        "FL",
        "GA",
        "HI",
        "ID",
        "IL",
        "IN",
        "IA",
        "KS",
        "KY",
        "LA",
        "ME",
        "MD",
        "MA",
        "MI",
        "MN",
        "MS",
        "MO",
        "MT",
        "NE",
        "NV",
        "NH",
        "NJ",
        "NM",
        "NY",
        "NC",
        "ND",
        "OH",
        "OK",
        "OR",
        "PA",
        "RI",
        "SC",
        "SD",
        "TN",
        "TX",
        "UT",
        "VT",
        "VA",
        "WA",
        "WV",
        "WI",
        "WY",
    ]


def generate_random_address():
    us_cities = fetch_us_cities()
    us_states = fetch_us_states()

    address_formats = [
        # Format 1: Street Address, City, State, Postal Code, United States
        "{street_address}, {city}, {state} {postal_code}, United States",
        # Format 2: Street Address, City, State, United States, Postal Code
        "{street_address}, {city}, {state}, United States {postal_code}",
        # Format 3: City, State, Postal Code, United States
        "{city}, {state} {postal_code}, United States",
        # Format 4: Postal Code, City, State, United States
        "{postal_code}, {city}, {state}, United States",
        # Format 5: City, State, United States
        "{city}, {state}, United States",
        # Format 6: Street Address, City, United States, Postal Code
        "{street_address}, {city}, United States {postal_code}",
    ]

    # Random address components
    street_address = (
        " ".join(random.sample(us_cities, random.randint(1, 3))) + " Street"
    )
    city = random.choice(us_cities)
    state = random.choice(us_states)
    postal_code = "".join(random.choices(string.digits, k=5))

    # Choose a random format
    address_format = random.choice(address_formats)

    # Generate the random address using the chosen format
    random_address = address_format.format(
        street_address=street_address,
        city=city,
        state=state,
        postal_code=postal_code,
    )

    return random_address


# Test the function to generate 10 random addresses
for _ in range(10):
    print(generate_random_address())
