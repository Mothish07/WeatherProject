import requests
import os

def uvIndexData(latitude, longitude):
    api_key = '91e35b107a50bb5769307b4aaca1fef4'
    #url Api Call
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}'
   

    #response getter
    response = requests.get(url)
    

    # Check the HTTP status code
    if response.status_code == 200:
        #getting json data
        uv_index = response.json()

        uv_index = uv_index.get('uvi', 0)

        if uv_index <= 2:
            return_data ={'info':'No protection Needed','uvIndex':uv_index}
        elif uv_index <=5:
            return_data = {'info':'Some Protection is required ','uvIndex':uv_index}
        elif uv_index <=7:
            return_data = {'info':'Protection Essential','uvINdex':uv_index}
        elif uv_index <=10:
            return_data = {'info':'Extra parotection Needed','uvIndex':uv_index}
        else:
            return_data = {'info':'Stay Inside','unIndex':uv_index}

        return return_data
    else:
        return {'success': False, 'response': 'Something Went Wrong Please Try again !'}

check = uvIndexData(11.635250, 78.148880)
print(check)

