import requests
from pprint import pprint

API_key = 'ba731702d39de09cd6aaedc8212a36c7'
city = input('Enter the city to check weather: ')

base_url = 'https://api.openweathermap.org/data/2.5/weather?appid='+API_key+'&q='+city

wather_data = requests.get(base_url).json()

pprint(wather_data)