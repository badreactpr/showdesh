import json
import requests

def handler(request, response):
    url = "https://otp-api.shelex.dev/api/countries"
    headers = {
        "authority": "otp-api.shelex.dev",
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.9",
        "origin": "https://otp.shelex.dev",
        "referer": "https://otp.shelex.dev/",
        "sec-ch-ua": '"Not A(Brand";v="8", "Chromium";v="132"',
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": '"Android"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36"
    }

    try:
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            countries = r.json()
            result = []
            for item in countries:
                result.append({
                    "url": item.get("url", ""),
                    "country": item.get("country", ""),
                    "source": item.get("source", ""),
                    "count": item.get("count", "")
                })
            return response.json(result)
        else:
            return response.json({"error": "Failed to fetch data", "status": r.status_code}, status=500)
    except Exception as e:
        return response.json({"error": str(e)}, status=500)
