import requests
import smtplib


api_key = "your open weather api key"
city = "your city"
my_lat = "your latitude"
my_long = "your longitude"
# open weather url endpoint
owm_url = "https://api.openweathermap.org/data/2.5/onecall"
weather_params = {
    "lat": my_lat,
    "lon": my_long,
    "appid": api_key,
    "exclude": "current,minutely,daily,alerts"
}


request = requests.get(url=owm_url, params=weather_params)
request.raise_for_status()
data = request.json()
hourly_data = data["hourly"][:13]

will_rain = False
for data in hourly_data:
   weather_id = data["weather"][0]["id"]
   if int(weather_id) <= 700:
    will_rain = True



my_email = "your email"
password = "your password"
receiver = "receiver email"
message  = "It's going to rain today, don't forget the umbrella if you go out!"


if will_rain:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        fmt = 'From: {}\r\nTo: {}\r\nSubject: {}\r\n{}'
        connection.sendmail(
            my_email,
            receiver,
            fmt.format(my_email, receiver, "Weather Alert", message).encode('utf-8')
        )