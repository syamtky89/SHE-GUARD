import requests

class LocationTool:

    def get_location(self):
        """
        Returns approximate location using IP-based geolocation.
        """

        try:
            response = requests.get("https://ipinfo.io/json")
            data = response.json()

            # Default fallback for missing values
            loc = data.get("loc", "0,0")

            latitude, longitude = loc.split(",")

            return {
                "ip": data.get("ip", "Unknown"),
                "city": data.get("city", "Unknown"),
                "region": data.get("region", "Unknown"),
                "country": data.get("country", "Unknown"),
                "latitude": latitude,
                "longitude": longitude,
                "provider": "ipinfo.io"
            }

        except Exception as e:
            return {"error": str(e)}
