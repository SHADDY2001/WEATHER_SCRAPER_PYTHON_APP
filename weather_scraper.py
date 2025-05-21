import requests
from bs4 import BeautifulSoup

def get_weather(city):
    url = f"https://wttr.in/{city}?format=%t"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text.strip()
    else:
        return None

def main():
    city = input("Enter city name: ")
    temp = get_weather(city)
    if temp:
        print(f"Current temperature in {city}: {temp}")
    else:
        print("Could not fetch weather data.")

if __name__ == "__main__":
    main()
