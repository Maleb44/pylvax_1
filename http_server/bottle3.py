from bottle import route, run

import requests

url_template = 'https://api.forecast.io/forecast/{api}/{lat},{lon}'
apikey = 'e2fd60c047ae3fac95a0618a98a9e5fd'


def get_temperature_lat_lon(lat, lon):
    url = url_template.format(api=apikey, lat=lat, lon=lon)

    params_dict = {
        'units': 'si'
    }

    r = requests.get(url, params=params_dict)
    if not r.ok:
        return 'error'

    data = r.json()
    temp = data['currently']['temperature']
    return temp


@route('/temperature/<lat>/<lon>')
def temperature_lat_lon(lat, lon):
    lat = float(lat)
    lon = float(lon)
    temp = get_temperature_lat_lon(lat, lon)
    return str(temp)


run(host='localhost', port=8080, debug=True)
