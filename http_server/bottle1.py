import datetime

from bottle import route, run


@route('/hello')
@route('/hello/<name>')
@route('/hello/<name>/<width>')
def hello(name='valaki', width=300):
    name_title = name.title()

    output_template = 'Hello {img}{name}!'

    if name == 'eniko':
        img = '<img src="http://polomania.hu/images/designs/tn3/1987904494512cb7497ee46.jpg" width={width}>'\
            .format(width=width)
    else:
        img = ''

    return output_template.format(img=img, name=name_title)


@route('/sq/<number>')
def sq(number):
    number = float(number)
    return str(number ** 2)


@route('/palindrom/<word>')
def is_palindrom(word):
    result = word == word[::-1]
    return str(result)


# GMT - Greenwich Mean Time, bad
# UTC - 0 timezone, no daylight saving time, good!!!

@route('/time_now')
def time_now():
    t = datetime.datetime.utcnow()
    return t.isoformat()


run(host='localhost', port=8080, debug=True)
