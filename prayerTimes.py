import requests

def fetchPrayerTime(city, country, month, year):

    req = requests.get(f"http://api.aladhan.com/v1/calendarByCity?city={city}&country={country}&method=2&month={month}&year={year}")
    response = req.json()

    return response['data']
# fetchPrayerTime("Dushanbe", "Tajikistan", "02", "2023")
