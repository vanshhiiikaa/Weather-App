import requests


API_KEY = "YOUR_API_KEY"


def get_weather(city):
    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={API_KEY}&units=metric"
    )

    try:
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            city_name = data["name"]
            country = data["sys"]["country"]
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            description = data["weather"][0]["description"]

            print("\n🌤 Weather Report")
            print("---------------------")
            print(f"Location: {city_name}, {country}")
            print(f"Temperature: {temperature}°C")
            print(f"Humidity: {humidity}%")
            print(f"Condition: {description}")

        else:
            print("❌ City not found")

    except Exception as e:
        print("Error:", e)


print("===== Weather App =====")

city = input("Enter city name: ")

get_weather(city)