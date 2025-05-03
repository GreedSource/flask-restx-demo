from flask import json
import requests


class ExampleService:

    def __init__(self):
        pass

    def get_currencies(self):
        url = "https://restcountries.com/v3.1/all"
        response = requests.get(url)

        if response.status_code == 200:
            countries = response.json()
            currencies = {}

            for country in countries:
                if "currencies" in country:
                    for code, details in country["currencies"].items():
                        currencies[code] = details.get("name", "Unknown Currency")

            # Convert to a list of objects
            currency_list = [
                {"currency": code, "name": name}
                for code, name in sorted(currencies.items())
            ]

            # Print formatted JSON output
            return currency_list
        else:
            return f"Failed to fetch data. Status code: {response.status_code}"
