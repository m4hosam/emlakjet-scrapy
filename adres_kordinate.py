import requests
from google_api_key import google_api_key_secret

def geocode_address(address):
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={google_api_key_secret}"
    response = requests.get(url)
    data = response.json()
    if data['status'] == 'OK':
        # Extract latitude and longitude
        lat = data['results'][0]['geometry']['location']['lat']
        lng = data['results'][0]['geometry']['location']['lng']
        return lat, lng
    else:
        print(f"Geocoding failed: {data['status']}")
        return None

# 29.43486713,40.81911964
# Example usage
if __name__ == "__main__":
    address = "Kocaeli - Gebze - İnönü Mahallesi"
    latitude, longitude = geocode_address(address)
    if latitude and longitude:
        print(f"Latitude: {latitude}, Longitude: {longitude}")
    else:
        print("Failed to geocode the address.")
