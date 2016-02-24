import requests

# Budapest
longitude = 19.05
latitude = 47.53

url_template = 'https://api.forecast.io/forecast/{api}/{lat},{lon}'
apikey = 'e2fd60c047ae3fac95a0618a98a9e5fd'

url = url_template.format(api=apikey, lat=latitude, lon=longitude)
# print url

params_dict = {
    'units': 'si'
}


r = requests.get(url, params=params_dict)
if r.ok:
    data = r.json()

    # import json
    # data2 = json.loads(r.text)
    # print data == data2

