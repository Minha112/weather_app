import requests
from config import API_KEY

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={API_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        desc = data['weather'][0]['description']

        print(f"\nWeather in {city}:")
        print(f"Temperature : {temp}°C")
        print(f"Humidity    : {humidity}%")
        print(f"Condition   : {desc.capitalize()}")
    else:
        print("\nCity not found. Please try again.")

def main():
    print("=== Simple Weather App ===")
    city = input("Enter city name: ")
    get_weather(city)

if __name__ == "__main__":
    main()
