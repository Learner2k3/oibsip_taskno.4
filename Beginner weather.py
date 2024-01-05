import requests

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}  

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  

        weather_data = response.json()

        temperature = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        description = weather_data["weather"][0]["description"]

        return {
            "temperature": temperature,
            "humidity": humidity,
            "description": description,
        }

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    except KeyError as key_err:
        print(f"Key error occurred: {key_err}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    api_key = "e674cf2f8c47df10a43dfddb8ab2a29e"
    
    if api_key == "e674cf2f8c47df10a43d":
        print("Please replace 'e674cf2f8c47df10a43d' with your actual API key.")
        return

    city = input("Enter the city name: ")

    weather_info = get_weather(api_key, city)

    if weather_info:
        print(f"Weather in {city}:")
        print(f"Temperature: {weather_info['temperature']} °C")
        print(f"Humidity: {weather_info['humidity']}%")
        print(f"Description: {weather_info['description']}")

if __name__ == "__main__":
    main()
