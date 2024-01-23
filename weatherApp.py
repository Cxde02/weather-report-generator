import requests
from datetime import datetime
import pytz

api_key = 'xxx'

while True:
    city = input('Enter city name [Press Enter to exit]: ')
    # Check if the user pressed Enter (empty string)
    if not city:
        print('Exiting the program. Goodbye!')
        break


    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

    local_timezone = pytz.timezone('Etc/GMT+4')

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        desc = data['weather'][0]['description']
        feels_like = data['main']['feels_like']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        wind_deg = data['wind']['deg']
        #sunrise = data['sys']['sunrise']
        #sunset = data['sys']['sunset']
    
        #Remove 12 hours
        sunrise_timestamp = data['sys']['sunrise'] - (12 * 60 * 60)
        #sunrise_datetime = datetime.utcfromtimestamp(sunrise_timestamp)
        #sunrise_str = sunrise_datetime.strftime("%H:%M")

        sunset_timestamp = data['sys']['sunset']
        #sunset_datetime = datetime.utcfromtimestamp(sunset_timestamp)
        #sunset_str = sunset_datetime.strftime("%H:%M")
    
        sunrise_datetime = datetime.utcfromtimestamp(sunrise_timestamp).astimezone(local_timezone)
        sunrise_str = sunrise_datetime.strftime("%H:%M")

        sunset_datetime = datetime.utcfromtimestamp(sunset_timestamp).astimezone(local_timezone)
        sunset_str = sunset_datetime.strftime("%H:%M")

        def printInfo():
            print(f'\nTemperature: {round(temp - 273.15, 2)} °C (feels like: {round(feels_like - 273.15, 2)} °C)')
            print('----------------------------------------------------------------')
            print(f'Description: {desc}')
            print('----------------------------------------------------------------')
            print(f'Humidity: {humidity}%')
            print('----------------------------------------------------------------')
            print(f'Wind: {wind_speed} km/h from {wind_deg}°')
            print('----------------------------------------------------------------')
            print(f'Sunrise (local time): {sunrise_str} am')
            print('----------------------------------------------------------------')
            print(f'Sunset (local time): {sunset_str} pm')
            print('----------------------------------------------------------------')

            if 'rain' in data:
                    precipitation = data['rain']['1h']  # Precipitation in the last 1 hour
                    print(f"Current precipitation in {city}: {precipitation} mm")
                    print('----------------------------------------------------------------')
            else:
                    print(f"No precipitation data available for {city}")
                    print('----------------------------------------------------------------')


        printInfo()

        #Statements--
        if temp < 10:
            print('\nDress warmly!\n')
        elif temp > 35:
            print('\nStay hydrated and avoid direct sunlight!\n')

    

    else:
        print('Error fetching weather data')


