import requests, os
from datetime import datetime, timezone
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.environ.get("CG_API_KEY")


def get_coin_data(total_pages=2):
    all_data = []

    page = 1
    while page <= total_pages:
        query = f"?vs_currency=cad&per_page=250&page={page}"
        URL = f"https://api.coingecko.com/api/v3/coins/markets{query}"
        headers = {"accept": "application/json", "x-cg-demo-api-key": API_KEY}

        response = requests.get(URL, headers=headers)

        if response.status_code == 200:
            all_data.extend(response.json())
            page += 1
        else:
            return None

    return all_data


def to_dict(data):
    return {
        "name": data["name"],
        "symbol": data["symbol"],
        "current_price": data["current_price"],
        "market_cap": data["market_cap"],
        "total_supply": data["total_supply"],
        "high_24h": data["high_24h"],
        "low_24h": data["low_24h"],
        "ath": data["ath"],
        "ath_date": data["ath_date"],
        "atl": data["atl"],
        "atl_date": data["atl_date"],
        "last_updated": data["last_updated"],
        "save_timestamp": datetime.now(timezone.utc),
    }
