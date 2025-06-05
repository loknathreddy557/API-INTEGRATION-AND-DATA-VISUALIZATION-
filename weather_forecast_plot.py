import requests
import matplotlib.pyplot as plt
import seaborn as sns

# Set Seaborn style
sns.set(style="darkgrid")

# OpenWeatherMap API setup
API_KEY = 'd34c115192df76bf8263dacec0d0a517'
CITY = 'Mumbai'
URL = f'https://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric'

# Fetch data from API
response = requests.get(URL)
data = response.json()

# Print response for debugging
print(data)

# Check if 'list' is in response
if 'list' in data:
    dates = []
    temperatures = []

    for item in data['list']:
        dates.append(item['dt_txt'])
        temperatures.append(item['main']['temp'])

    # Visualization
    plt.figure(figsize=(14, 6))
    plt.plot(dates, temperatures, marker='o', color='skyblue')
    plt.xticks(rotation=45)
    plt.title(f"5-Day Temperature Forecast for {CITY}")
    plt.xlabel("Date & Time")
    plt.ylabel("Temperature (°C)")
    plt.tight_layout()
    plt.show()
else:
    print("Error fetching data:", data.get("message", "Unknown error"))
