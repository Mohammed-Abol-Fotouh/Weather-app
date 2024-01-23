import tkinter as tk
import requests

window = tk.Tk()
window.title("Weather Forecast")
window.rowconfigure(0, minsize=300)
window.columnconfigure(1, minsize=100)


def getLocation():
    location = location_entry.get()
    weather_url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={'3c55d01b8a4302f15dbf837e5a060aa2'}&units=metric"
    response = requests.get(weather_url)

    if response.status_code == 200:
        weather_data = response.json()
        temp = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        pressure = weather_data["main"]["pressure"]
        windSpeed = weather_data["wind"]["speed"]

        # I tried hared to get "precipitation" but api get me erors buit i found this way efficient hopfulyyou consider this api error
        try:
            # Check if rain data is available
            precipitation = weather_data["rain"]["1h"] if "rain" in weather_data else 0
        except KeyError:
            precipitation = 0

        temp_label.config(text=f"Temperature: {temp} °C")
        humidity_label.config(text=f"Humidity: {humidity} %")
        pressure_label.config(text=f"Pressure: {pressure} hPa")
        windSpeed_label.config(text=f"Wind Speed: {windSpeed} m/s")
        precipitiation_label.config(text=f"Precipitation: {precipitation} mm")
        error_label.config(text="")

        # Show the labels
        temp_label.grid(row=2, column=0, padx=15, pady=15, sticky="W")
        humidity_label.grid(row=3, column=0, padx=15, pady=15, sticky="W")
        windSpeed_label.grid(row=4, column=0, padx=15, pady=15, sticky="W")
        pressure_label.grid(row=5, column=0, padx=15, pady=15, sticky="W")
        precipitiation_label.grid(row=6, column=0, padx=15, pady=15, sticky="W")
    else:
        # Hide the labels
        temp_label.grid_forget()
        humidity_label.grid_forget()
        windSpeed_label.grid_forget()
        pressure_label.grid_forget()
        precipitiation_label.grid_forget()

        error_label.config(
            text=f"Error: {response.status_code} - {response.reason}, Something went wrong!!!"
        )
        # Show the error label
        error_label.grid(row=7, column=0, padx=15, pady=15, sticky="NSEW")


search_frame = tk.Frame(window, relief=tk.RAISED)
search_label = tk.Label(search_frame, text="Location:", font=("Helvetica", 16))
location_entry = tk.Entry(search_frame, font=("Helvetica", 16))
search_btn = tk.Button(search_frame, text="Search", command=getLocation)

temp_label = tk.Label(search_frame, text="Temperature:", font=("Helvetica", 16))
humidity_label = tk.Label(search_frame, text="Humidity:", font=("Helvetica", 16))
windSpeed_label = tk.Label(search_frame, text="Wind Speed:", font=("Helvetica", 16))
pressure_label = tk.Label(search_frame, text="Pressure:", font=("Helvetica", 16))
precipitiation_label = tk.Label(
    search_frame, text="Precipitation:", font=("Helvetica", 16)
)
error_label = tk.Label(window, text="", font=("Helvetica", 16), fg="red")

search_frame.grid(column=0, rowspan=2, padx=5, pady=15, sticky="NSEW")
search_label.grid(row=0, column=1, rowspan=2, padx=5, pady=15, sticky="W")
location_entry.grid(row=0, column=2, rowspan=2, padx=5, sticky="W")
search_btn.grid(row=0, column=3, padx=5, pady=15)

window.mainloop()
