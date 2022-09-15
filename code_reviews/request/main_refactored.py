"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import requests

URL: str = "https://www.freeforexapi.com/api/live?pairs="


def get_rate(url: str, currency: str) -> float:
    response = requests.get(f"{url}{currency}")
    data = response.json()
    return data["rates"][currency]["rate"]


if __name__ == "__main__":
    rate = get_rate(URL, "USDCOP")
    print(rate)
