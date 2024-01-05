import tkinter as tk
from tkinter import ttk, messagebox
from geopy.geocoders import Nominatim
import requests

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather App")
        self.root.geometry("400x400")

        self.label_city = ttk.Label(root, text="City:")
        self.label_city.pack(pady=10)

        self.entry_city = ttk.Entry(root)
        self.entry_city.pack(pady=10)

        self.button_get_weather = ttk.Button(root, text="Get Weather", command=self.get_weather)
        self.button_get_weather.pack(pady=10)

        self.label_result = ttk.Label(root, text="")
        self.label_result.pack(pady=10)

    def get_weather(self):
        city = self.entry_city.get()

        if not city:
            messagebox.showerror("Error", "Please enter a city.")
            return

        try:
            location = self.get_location(city)
            weather_data = self.get_weather_data(location.latitude, location.longitude)

            result_text = f"Weather in {city}:\n"
            result_text += f"Temperature: {weather_data['temperature']} °C\n"
            result_text += f"Humidity: {weather_data['humidity']}%\n"
            result_text += f"Description: {weather_data['description']}\n"
            result_text += f"Wind Speed: {weather_data['wind_speed']} m/s"

            self.label_result.config(text=result_text)

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def get_location(self, city):
        geolocator = Nominatim(user_agent="weather_app")
        location = geolocator.geocode(city)
        if not location:
            raise ValueError("Location not found.")
        return location

    def get_weather_data(self, latitude, longitude):
        api_key = "e674cf2f8c47df10a43dfddb8ab2a29e"
        base_url = "http://api.openweathermap.org/data/2.5/weather"
        params = {"lat": latitude, "lon": longitude, "appid": api_key, "units": "metric"}

        response = requests.get(base_url, params=params)
        response.raise_for_status()

        weather_data = response.json()

        temperature = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        description = weather_data["weather"][0]["description"]
        wind_speed = weather_data["wind"]["speed"]

        return {
            "temperature": temperature,
            "humidity": humidity,
            "description": description,
            "wind_speed": wind_speed,
        }

if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()
