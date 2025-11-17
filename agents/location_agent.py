import requests

class LocationAgent:
    def get_location(self):
        try:
            print("[LocationAgent] Detecting IP-based location...")
            response = requests.get("http://ip-api.com/json/")
            data = response.json()

            if data["status"] == "success":
                city = data.get("city", "")
                region = data.get("regionName", "")
                country = data.get("country", "")
                lat = data.get("lat", "")
                lon = data.get("lon", "")

                location = f"{city}, {region}, {country} (Lat: {lat}, Lon: {lon})"
                print("[LocationAgent] Location:", location)
                return location

            return "Unknown Location"

        except Exception as e:
            print("[LocationAgent] Error:", e)
            return "Location Error"
