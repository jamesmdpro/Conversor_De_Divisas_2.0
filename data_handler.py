import requests


def get_exchange_rate(pesos):
    base_url = "https://www.freeforexapi.com/api/live?pairs="
    currencies = {
        1: "USDCOP",
        2: "USDCOP",
        3: "USDMXN",
        4: "USDMXN",
        5: "USDPEN"
    }

    try:
        currency_pair = currencies[pesos["conversion"]]
        url = base_url + currency_pair
        response = requests.get(url)
        response.raise_for_status()  # raise exception for invalid status codes
        data = response.json()
        rate = data["rates"][currency_pair]["rate"]
        return float(rate)
    except (KeyError, requests.exceptions.RequestException, ValueError) as e:
        # handle exceptions and return error message
        return f"Error: {str(e)}"
