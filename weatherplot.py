import matplotlib.pyplot as plt




def display_weather(weather_data):
    if weather_data['success']:
        categories = ['Temperature', 'Humidity', 'Wind Speed', 'Rain', 'Snow', 'Pressure', 'Cloud Coverage']
        values = [
            float(weather_data['temperature']),
            int(weather_data['humidity']),
            float(weather_data['wind_speed']),
            0 if 'No' in weather_data['rain'] else float(weather_data['rain']),
            0 if 'No' in weather_data['snow'] else float(weather_data['snow']),
            int(weather_data['atmospheric_pressure']),
            int(weather_data['cloud_coverage_percentage'])
            
        ]
        colors = ['#FF6347', '#87CEEB', '#98FB98', '#4682B4', '#B0C4DE', '#FFD700', '#A9A9A9']

        plt.figure(figsize=(10, 6))
        plt.barh(categories, values, color=colors)
        plt.title('Current Weather Information')
        plt.xlabel('Values')
        plt.grid(axis='x', linestyle='--', alpha=0.6)

        for i, value in enumerate(values):
            plt.text(value, i, str(value), ha='left' if isinstance(value, (int, float)) else 'right', va='center', fontsize=10, color='black')

        image_filename = f'/home/mothish/Projects/ArulminiProject/static/weatherappImage/weatherGraph.png'
        plt.savefig(image_filename)
        plt.close()

        
    