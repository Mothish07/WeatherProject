import requests

def solarRadiationData(latitude, longitude):
    api_key = '91e35b107a50bb5769307b4aaca1fef4'
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}'

    response = requests.get(url)

    if response.status_code == 200:
        weather_data = response.json()

        # Check if solar radiation data is available
        if 'current' in weather_data and 'rad' in weather_data['current']:
            solar_radiation = weather_data['current']['rad']
            return {'success': True, 'solar_radiation': solar_radiation}
        else:
            return {'success': False, 'response': 'Solar radiation data not available for this location'}
    else:
        return {'success': False, 'response': 'Something Went Wrong. Please Try again!'}

# Example usage
solar_data = solarRadiationData(11.635250, 78.148880)
print(solar_data)
