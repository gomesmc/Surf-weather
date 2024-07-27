import requests
from pprint import pprint

API_KEY = '158e06224fcb20a446653586de5b6705'
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather_data(city, api_key):
    try:
        response = requests.get(BASE_URL, params={'q': city, 'appid': api_key})
        response.raise_for_status()  # Check if the request was successful
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")
    return None

def convert_kelvin_to_celsius(temp_kelvin):
    return temp_kelvin - 273.15

def print_weather_conditions(weather_data):
    temp = convert_kelvin_to_celsius(weather_data['main']['temp'])
    wind_speed = weather_data['wind']['speed']
    weather_description = weather_data['weather'][0]['description']
    visibility = weather_data.get('visibility', 'N/A')
    cloud_coverage = weather_data['clouds']['all']

    print("\nCondições do tempo para hoje:")
    print("**********************************")
    print(f"Temperatura: {temp:.2f}°C")
    print(f"Velocidade do Vento: {wind_speed} m/s")
    print(f"Descrição do Tempo: {weather_description}")
    print(f"Visibilidade: {visibility} m")
    print(f"Nível de Nuvens: {cloud_coverage}%")
    print("***********************************")

    check_surf_conditions(temp, wind_speed, visibility, cloud_coverage)

def check_surf_conditions(temp, wind_speed, visibility, cloud_coverage):
    safe_to_surf = True
    
    if temp < 20 or temp > 30:
        print("\nA temperatura não é ideal para surfar.")
        safe_to_surf = False

    if wind_speed > 10:
        print("\nOs ventos estão muito fortes para surfar.")
        safe_to_surf = False

    if visibility != 'N/A' and visibility < 1000:
        print("\nA visibilidade está muito baixa para surfar.")
        safe_to_surf = False

    if cloud_coverage > 75:
        print("\nHá muitas nuvens, o que pode afetar a visibilidade.")
        safe_to_surf = False

    if safe_to_surf:
        print("\nAs condições são boas para surfar!")

def main():
    print("Aloha, vamos checar as condições de surf para hoje\n")
    city = input('Digite o nome de uma cidade: ')
    
    weather_data = get_weather_data(city, API_KEY)
    
    if weather_data:
        print_weather_conditions(weather_data)
    else:
        print("Não foi possível obter os dados meteorológicos.")

main()
