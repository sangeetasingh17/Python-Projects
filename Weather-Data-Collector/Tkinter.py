# ===== imports =======
import json
from urllib.request import urlopen
from API_key import api_key
from html.parser import HTMLParser
from tkinter import scrolledtext
import urllib.request
import tkinter as tk
from tkinter import Menu
from tkinter import ttk

# ===== functions ======

# Exit GUI cleanly


def _quit():
    win.quit()
    win.destroy()
    exit()


# ===== procedural code =====

# Create instance
win = tk.Tk()

# Add a title
win.title("Weather Conditons")
# ---------------------------------------------------------------
# Creating a Menu Bar
menuBar = Menu()
win.config(menu=menuBar)

# Add menu items
fileMenu = Menu(menuBar, tearoff=0)
fileMenu.add_command(label="New")
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=_quit)
menuBar.add_cascade(label="File", menu=fileMenu)

# Add another Menu to the Menu Bar and an item
helpMenu = Menu(menuBar, tearoff=0)
helpMenu.add_command(label="About")
menuBar.add_cascade(label="Help", menu=helpMenu)
# ---------------------------------------------------------------

# Tab Control / Notebook
tabControl = ttk.Notebook(win)          # Create Tab Control

tab1 = ttk.Frame(tabControl)            # Add a second tab
tabControl.add(tab1, text='OpenWeatherMap')      # Make second tab visible

tabControl.pack(expand=1, fill="both")  # Pack to make visible
# ---------------------------------------------------------------


# TAB 1 OpenWeatherMap
######################

# We are creating a container frame to hold other widgets
open_weather_cities_frame = ttk.LabelFrame(
    tab1, text=' Latest Observation for ')
open_weather_cities_frame.grid(column=0, row=0, padx=8, pady=4)

# Station City label
open_location = tk.StringVar()
ttk.Label(open_weather_cities_frame, textvariable=open_location).grid(
    column=0, row=1, columnspan=3)

# ---------------------------------------------------------------
# Adding a Label
ttk.Label(open_weather_cities_frame, text="City: ").grid(column=0, row=0)

# ---------------------------------------------------------------
open_city = tk.StringVar()
open_city_combo = ttk.Combobox(
    open_weather_cities_frame, width=16, textvariable=open_city)
open_city_combo['values'] = (
    'Los Angeles, US', 'London, UK', 'Paris, FR', 'Mumbai, IN', 'Beijing, CN')
open_city_combo.grid(column=1, row=0)
open_city_combo.current(0)                 # highlight first city station id

# ---------------------------------------------------------------

# callback function


def _get_station_open():
    city = open_city_combo.get()
    get_open_weather_data(city)


get_weather_btn = ttk.Button(open_weather_cities_frame, text='Get Weather',
                             command=_get_station_open).grid(column=2, row=0)

# ---------------------------------------------------------------
for child in open_weather_cities_frame.winfo_children():
    child.grid_configure(padx=5, pady=2)

# ---------------------------------------------------------------
# We are creating a container frame to hold all other widgets
open_weather_conditions_frame = ttk.LabelFrame(
    tab1, text=' Current Weather Conditions ')
open_weather_conditions_frame.grid(column=0, row=1, padx=8, pady=4)


ENTRY_WIDTH = 25

# Adding Label & Textbox Entry widgets
# ---------------------------------------------
ttk.Label(open_weather_conditions_frame, text="Last Updated:").grid(
    column=0, row=1, sticky='E')         # <== right-align
open_updated = tk.StringVar()
open_updatedEntry = ttk.Entry(open_weather_conditions_frame,
                              width=ENTRY_WIDTH, textvariable=open_updated, state='readonly')
open_updatedEntry.grid(column=1, row=1, sticky='W')
# ---------------------------------------------
ttk.Label(open_weather_conditions_frame, text="Weather:").grid(
    column=0, row=2, sticky='E')               # <== increment row for each
open_weather = tk.StringVar()
open_weatherEntry = ttk.Entry(open_weather_conditions_frame,
                              width=ENTRY_WIDTH, textvariable=open_weather, state='readonly')
# <== increment row for each
open_weatherEntry.grid(column=1, row=2, sticky='W')
# ---------------------------------------------
ttk.Label(open_weather_conditions_frame, text="Temperature:").grid(
    column=0, row=3, sticky='E')
open_temp = tk.StringVar()
open_tempEntry = ttk.Entry(open_weather_conditions_frame,
                           width=ENTRY_WIDTH, textvariable=open_temp, state='readonly')
open_tempEntry.grid(column=1, row=3, sticky='W')
# ---------------------------------------------
ttk.Label(open_weather_conditions_frame, text="Relative Humidity:").grid(
    column=0, row=5, sticky='E')
open_rel_humi = tk.StringVar()
open_rel_humiEntry = ttk.Entry(open_weather_conditions_frame,
                               width=ENTRY_WIDTH, textvariable=open_rel_humi, state='readonly')
open_rel_humiEntry.grid(column=1, row=5, sticky='W')
# ---------------------------------------------
ttk.Label(open_weather_conditions_frame, text="Wind:").grid(
    column=0, row=6, sticky='E')
open_wind = tk.StringVar()
open_windEntry = ttk.Entry(open_weather_conditions_frame,
                           width=ENTRY_WIDTH, textvariable=open_wind, state='readonly')
open_windEntry.grid(column=1, row=6, sticky='W')
# ---------------------------------------------
ttk.Label(open_weather_conditions_frame, text="Visibility:").grid(
    column=0, row=7, sticky='E')
open_visi = tk.StringVar()
open_visiEntry = ttk.Entry(open_weather_conditions_frame,
                           width=ENTRY_WIDTH, textvariable=open_visi, state='readonly')
open_visiEntry.grid(column=1, row=7, sticky='W')
# ---------------------------------------------
ttk.Label(open_weather_conditions_frame, text="Pressure:").grid(
    column=0, row=8, sticky='E')
open_msl = tk.StringVar()
open_mslEntry = ttk.Entry(open_weather_conditions_frame,
                          width=ENTRY_WIDTH, textvariable=open_msl, state='readonly')
open_mslEntry.grid(column=1, row=8, sticky='W')
# ---------------------------------------------
ttk.Label(open_weather_conditions_frame, text="Sunrise:").grid(
    column=0, row=9, sticky='E')
sunrise = tk.StringVar()
sunriseEntry = ttk.Entry(open_weather_conditions_frame,
                         width=ENTRY_WIDTH, textvariable=sunrise, state='readonly')
sunriseEntry.grid(column=1, row=9, sticky='E')
# ---------------------------------------------
ttk.Label(open_weather_conditions_frame, text="Sunset:").grid(
    column=0, row=10, sticky='E')
sunset = tk.StringVar()
sunsetEntry = ttk.Entry(open_weather_conditions_frame,
                        width=ENTRY_WIDTH, textvariable=sunset, state='readonly')
sunsetEntry.grid(column=1, row=10, sticky='E')
# ---------------------------------------------

# Add some space around each widget
for child in open_weather_conditions_frame.winfo_children():
    child.grid_configure(padx=4, pady=2)

# =============== OpenWeatherMap Data collection ===========


def get_open_weather_data(city='London,uk'):
    city = city.replace(' ', '%20')
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(
        city, api_key)
    response = urlopen(url)
    data = response.read().decode()
    json_data = json.loads(data)

    from pprint import pprint
    pprint(json_data)

    lat_long = json_data['coord']
    lastupdate_unix = json_data['dt']
    city_id = json_data['id']
    humidity = json_data['main']['humidity']
    pressure = json_data['main']['pressure']
    temp_kelvin = json_data['main']['temp']
    city_name = json_data['name']
    city_country = json_data['sys']['country']
    sunrise_unix = json_data['sys']['sunrise']
    sunset_unix = json_data['sys']['sunset']
    try:
        visibility_meter = json_data['visibility']
    except:
        visibility_meter = 'N/A'
    owm_weather = json_data['weather'][0]['description']
    weather_icon = json_data['weather'][0]['icon']
    wind_deg = json_data['wind']['deg']
    wind_speed_meter_sec = json_data['wind']['speed']

    def kelvin_to_celsius(temp_k):
        return "{:.1f}".format(temp_k - 273.15)

    def kelvin_to_fahrenheit(temp_k):
        return "{:.1f}".format((temp_k - 273.15) * 1.8000 + 32.00)

    from datetime import datetime

    def unix_to_datetime(unix_time):
        return datetime.fromtimestamp(int(unix_time)
                                      ).strftime('%Y-%m-%d %H:%M:%S')

    def meter_to_miles(meter):
        return "{:.2f}".format((meter * 0.00062137))

    if visibility_meter is 'N/A':
        visibility_miles = 'N/A'
    else:
        visibility_miles = meter_to_miles(visibility_meter)

    def mps_to_mph(meter_second):
        return "{:.1f}".format((meter_second * (2.23693629)))

    # -------------------------------------------------------
    # Update GUI entry widgets with live data
    open_location.set('{}, {}'.format(city_name, city_country))

    lastupdate = unix_to_datetime(lastupdate_unix)
    open_updated.set(lastupdate)
    open_weather.set(owm_weather)
    temp_fahr = kelvin_to_fahrenheit(temp_kelvin)
    temp_cels = kelvin_to_celsius(temp_kelvin)
    open_temp.set('{} \xb0F  ({} \xb0C)'.format(temp_fahr, temp_cels))
    open_rel_humi.set('{} %'.format(humidity))
    wind_speed_mph = mps_to_mph(wind_speed_meter_sec)
    open_wind.set('{} degrees at {} MPH'.format(wind_deg, wind_speed_mph))
    open_visi.set('{} miles'.format(visibility_miles))
    open_msl.set('{} hPa'.format(pressure))
    sunrise_dt = unix_to_datetime(sunrise_unix)
    sunrise.set(sunrise_dt)
    sunset_dt = unix_to_datetime(sunset_unix)
    sunset.set(sunset_dt)

    # win.update()        # required or we won't see the icon

# =========== Start GUI ===================


win.mainloop()
