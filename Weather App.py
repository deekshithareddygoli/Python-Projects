import requests

api_key = '8e7671090a34afb8ba8e61f4281c0233'

user_input = input("Enter the City: ")
weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

if weather_data.json()['cod'] == '404':
    print("No City Found")
else:
    weather = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])
    humidity = weather_data.json()['main']['humidity']
    wind_speed = weather_data.json()['wind']['speed']
    sun_rise = weather_data.json()['sys']['sunrise']
    sun_set = weather_data.json()['sys']['sunset']

    print(f"The Weather in {user_input} is: {weather}")
    print(f"The Temperature in {user_input} is: {temp}°F")
    print(f"Humidity in {user_input} is: {humidity}%")
    print(f"Wind Speed in {user_input} is: {wind_speed}m/s")
    print(f"Sun rises in {user_input} at {sun_rise}")
    print(f"Sun sets in {user_input} at {sun_set}")