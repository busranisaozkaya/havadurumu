import requests

from datetime import datetime


def day_name(date_str):
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    day_names = ['Pazartesi', 'Salı', 'Çarşamba', 'Perşembe', 'Cuma', 'Cumartesi', 'Pazar']
    return day_names[date_obj.weekday()]


def get_weather(city):
    api_key = "aa9a49fef9cf41ccb6a215004231410"
    url = f"http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={city}&days=3&lang=tr"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        processed_weather_data = []
        for forecast in data['forecast']['forecastday']:
            processed_weather_data.append({
                'turkish_day': day_name(forecast['date']),
                'date': forecast['date'],
                'condition': forecast['day']['condition']['text'],
                'max_temp': forecast['day']['maxtemp_c'],
                'min_temp': forecast['day']['mintemp_c']
            })
        return processed_weather_data, data
    else:
        return None
