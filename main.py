import click
import requests
import openweatherconfig as cfg

weatherapp_api = "https://api.openweathermap.org/data/2.5/weather?q="

@click.command()
@click.option('--city', prompt='Your city', help='The city you want to know the weather for')
def weather_now(city):
    url = weatherapp_api + city + "&appid=" + cfg.api_key
    try:
        res = requests.get(url)
        data = res.json()
        temp = data['main']['temp']
        wind_speed = data['wind']['speed']
        latitude = data['coord']['lat']
        longitude = data['coord']['lon']
        description = data['weather'][0]['description']
        print(f"Weather Stats for - {city.upper()} are as follows:")
        print(f"Temperature: {temp}")
        print(f"Wind Speed: {wind_speed}")
        print(f"Latitude: {latitude}")
        print(f"Longitude: {longitude}")
        print(f"Description: {description}")
    except:
        print("Please check your city name")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    weather_now()

