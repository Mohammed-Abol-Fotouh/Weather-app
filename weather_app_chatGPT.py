import tkinter as tk
from tkinter import StringVar
import requests


def get_location():
    # Get the location from the entry
    location = location_entry.get()
    if location:
        # Construct the API URL for weather data
        weather_url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid=3c55d01b8a4302f15dbf837e5a060aa2&units=metric"
        # Make a request to the API
        response = requests.get(weather_url)

        if response.status_code == 200:
            # Parse the JSON response
            weather_data = response.json()
            # Extract weather information
            temp = weather_data["main"]["temp"]
            humidity = weather_data["main"]["humidity"]
            pressure = weather_data["main"]["pressure"]
            wind_speed = weather_data["wind"]["speed"]

            try:
                # Check if rain data is available
                precipitation = (
                    weather_data["rain"]["1h"] if "rain" in weather_data else 0
                )
            except KeyError:
                precipitation = 0

            # Update the text variables for labels
            temp_var.set(f"Temperature: {temp} °C")
            humidity_var.set(f"Humidity: {humidity} %")
            pressure_var.set(f"Pressure: {pressure} hPa")
            wind_speed_var.set(f"Wind Speed: {wind_speed} m/s")
            precipitation_var.set(f"Precipitation: {precipitation} mm")
            error_var.set("")

            # Show the labels
            show_labels()
        else:
            # Hide the labels
            hide_labels()
            # Update error label with error message
            error_var.set(
                f"Error: {response.status_code} - {response.reason}, Something went wrong!!!"
            )
            error_label.grid(row=7, column=0, padx=15, pady=15, sticky="NSEW")
    else:
        # Hide the labels
        hide_labels()
        # Update error label with a message to enter a location
        error_var.set("Error: Please enter a location")
        error_label.grid(row=7, column=0, padx=15, pady=15, sticky="NSEW")


def show_labels():
    # Show all the labels
    temp_label.grid(row=2, column=0, padx=15, pady=15, sticky="W")
    humidity_label.grid(row=3, column=0, padx=15, pady=15, sticky="W")
    wind_speed_label.grid(row=4, column=0, padx=15, pady=15, sticky="W")
    pressure_label.grid(row=5, column=0, padx=15, pady=15, sticky="W")
    precipitation_label.grid(row=6, column=0, padx=15, pady=15, sticky="W")


def hide_labels():
    # Hide all the labels
    temp_label.grid_forget()
    humidity_label.grid_forget()
    wind_speed_label.grid_forget()
    pressure_label.grid_forget()
    precipitation_label.grid_forget()


# Create the main window
window = tk.Tk()
window.title("Weather Forecast")
window.rowconfigure(0, minsize=300)
window.columnconfigure(1, minsize=100)

# Create the search frame
search_frame = tk.Frame(window, relief=tk.RAISED)
search_label = tk.Label(search_frame, text="Location:", font=("Helvetica", 16))
location_entry = tk.Entry(search_frame, font=("Helvetica", 16))
search_btn = tk.Button(search_frame, text="Search", command=get_location)

# Create StringVar variables for dynamic text updates
temp_var = StringVar()
humidity_var = StringVar()
wind_speed_var = StringVar()
pressure_var = StringVar()
precipitation_var = StringVar()
error_var = StringVar()

# Create labels with dynamic text
temp_label = tk.Label(search_frame, textvariable=temp_var, font=("Helvetica", 16))
humidity_label = tk.Label(
    search_frame, textvariable=humidity_var, font=("Helvetica", 16)
)
wind_speed_label = tk.Label(
    search_frame, textvariable=wind_speed_var, font=("Helvetica", 16)
)
pressure_label = tk.Label(
    search_frame, textvariable=pressure_var, font=("Helvetica", 16)
)
precipitation_label = tk.Label(
    search_frame, textvariable=precipitation_var, font=("Helvetica", 16)
)
error_label = tk.Label(window, textvariable=error_var, font=("Helvetica", 16), fg="red")

# Configure the grid layout for the search frame
search_frame.grid(column=0, rowspan=2, padx=5, pady=15, sticky="NSEW")
search_label.grid(row=0, column=1, rowspan=2, padx=5, pady=15, sticky="W")
location_entry.grid(row=0, column=2, rowspan=2, padx=5, sticky="W")
search_btn.grid(row=0, column=3, padx=5, pady=15)

# Start the Tkinter main loop
window.mainloop()
