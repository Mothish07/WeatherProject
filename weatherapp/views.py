from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from .forms import LocationForm
import json
from weatherData import currentWeatherData
from airData import currentAirData
from weatherplot import display_weather
from airplot import visualize_air_quality
from .models import FeedBack

def home(request):
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            latitude = form.cleaned_data['latitude']
            longitude = form.cleaned_data['longitude']
            data = {'latitude': latitude, 'longitude': longitude}
            filename = '/home/mothish/Projects/ArulminiProject/locationInfo.json'
            existing_data = read_json_file(filename)
            existing_data.update(data)

            with open(filename, 'w') as json_file:
                json.dump(existing_data, json_file)

            return render(request,'weatherapp/main.html')
    else:
        form = LocationForm()
    return render(request,'weatherapp/index.html')

def main(request):
    return render(request,'weatherapp/main.html')

def weatherdata(request):
    filename = '/home/mothish/Projects/ArulminiProject/locationInfo.json'
    location = read_json_file(filename)
    responce = currentWeatherData(location['latitude'], location['longitude'])
    display_weather(responce) # to update the weatherGraph Image
    if responce['success']:
        context = {
        'weatherDescription':responce['weather_description'],
        'temperature':responce['temperature'],
        'humidity':responce['humidity'],
        'windSpeed':responce['wind_speed'],
        'rain':responce['rain'],
        'snow':responce['snow'],
        'atmosphericPressure':responce['atmospheric_pressure']
        }
    else:
        context = {
        'weatherDescription':'#',
        'temperature':'#',
        'humidity':'#',
        'windSpeed':'#',
        'rain':'#',
        'snow':'#',
        'atmosphericPressure':'#'
        }

    return render(request,'weatherapp/weatherdata.html',context)

def airdata(request):
    filename = '/home/mothish/Projects/ArulminiProject/locationInfo.json'
    location = read_json_file(filename)
    responce = currentAirData(location['latitude'], location['longitude'])
    visualize_air_quality(responce)
    if responce['success']:
        context = {
            'airQualityCategory':responce['air_quality_category'],
            'pm25':responce['pm25'],
            'pm10':responce['pm10'],
            'o3':responce['o3'],
            'no2':responce['no2'],
            'so2':responce['so2'],
            'co':responce['co']
    }
    else:
        context = {
            'airQualityCategory':'#',
            'pm25':'#',
            'pm10':'#',
            'o3':'#',
            'no2':'#',
            'so2':'#',
            'co':'#'
    }

    return render(request,'weatherapp/airdata.html',context)

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        FeedBack.objects.create(name=name, email=email, message=message)
        return HttpResponse('Thank you for your feedback! <a href="{}">Return to Home page</a>'.format(reverse('main')))


    return render(request,'weatherapp/contact.html')

def read_json_file(filename):
    try:
        with open(filename, 'r') as json_file:
            data = json.load(json_file)
    except FileNotFoundError:
        data = {}
    return data
