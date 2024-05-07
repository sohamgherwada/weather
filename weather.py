import requests
import sys

def main():
    while True:
        city = input("Enter the city (or 'end' to exit): ")
        if city == "end":
            break
        
        city = city.replace(" ", "%20")
        api_key = "9151390c137bd7d44f059851314e63ca"
        base_url = f"http://api.weatherstack.com/current?access_key={api_key}&query={city}"
        
        response = requests.get(base_url)
        data = response.json()
        
        print(data['current']['temperature'],"°C")

main()