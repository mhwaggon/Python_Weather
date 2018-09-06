import urllib.request
import urlopen
import json


def get_ip_address():
    link = "http://checkip.dyndns.org"
    a = urlopen(link)
    ipinfo = a.read()
    ip_address = ipinfo[-30:-16]
    ip_address = str(ip_address)
    return ip_address


def get_weather(ip_address):
    base_url = "http://api.worldweatheronline.com/premium/v1/weather.ashx?"
    api_key = "key=INSERTAPIKEY"
    ip_call = "q=" + ip_address
    add_api_info = "&num_of_days=2&tp=3&showmap=yes&format=JSON"
    url = base_url + api_key + ip_call + add_api_info
    json_reader = urllib.urlopen(url).read()
    data = json.loads(json_reader)
    weather = data['data']['current_condition'[0]]
    return weather


def show_weather(weather):
    print(
        """
        Weather : {} 
        Temperature : {} 
        Feels Like: {}
        Humidity : {} 
        Precipitation : {}
        """).format(
        weather['weatherDesc'][0]['value'], weather['temp_F'], weather['FeelsLikeF'], weather['humidity'],
        weather['precipMM'])


def index():
    print("Obtaining the weather in your area...")
    ip_address = get_ip_address()
    your_weather = get_weather(ip_address)
    show_weather(your_weather)


