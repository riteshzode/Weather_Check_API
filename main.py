import requests
from twilio.rest import Client

api_url = "https://api.openweathermap.org/data/2.5/onecall?"
api_key = "WEATHER_MAP_API_KEY"

account_sid = "YOUR_ACCOUNT_ID"
auth_token = "YOUR_ACCOUNT_TOKEN"

twilio_from_no = "SENDER_NUMBER"
twilio_to_no = "RECEIVER_NUMBER"

my_lat = 19.852156
my_lon = 79.352093

parameter = {
    "lat": my_lat,
    "lon": my_lon,
    "appid": api_key,
    "exclude": "current,daily,minutely"
}

r = requests.get(api_url, params=parameter)
# print(r.json()['hourly'][:13])

is_rain = False

for i in r.json()['hourly'][:13]:
    if i['weather'][0]["id"] < 700:
        is_rain = True

if is_rain:
    print('Its going to rain today, please bring Umbrella ☂️')

    # we can send message by twilio or email

    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body='Its going to rain today, please bring Umbrella ☂️',
        from_=twilio_from_no,
        to=twilio_to_no
    )

    print(message.status)

