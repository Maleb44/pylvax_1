from bottle import route, run


@route('/hello')
@route('/hello/<name>')
def hello(name='valaki'):
    name_title = name.title()

    output_template = 'Hello {img}{name}!'

    if name == 'eniko':
        img = '<img src="http://polomania.hu/images/designs/tn3/1987904494512cb7497ee46.jpg">'
    else:
        img = ''

    return output_template.format(img=img, name=name_title)

run(host='localhost', port=8080, debug=True)
