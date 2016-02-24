import datetime

from bottle import request, route, run


# GMT - Greenwich Mean Time, bad
# UTC - 0 timezone, no daylight saving time, good!!!


@route('/time_now')
def time_now():
    t = datetime.datetime.utcnow()
    return t.isoformat()


@route('/multi/<num1>/<num2>')
@route('/multi/<num1>,<num2>')
def multiply(num1, num2):
    num1 = float(num1)
    num2 = float(num2)

    return str(num1 * num2)


# query parameters
# /multi?num1=12&num2=24

@route('/multi')
def multi_query():
    if 'num1' not in request.query or \
       'num2' not in request.query:
        return 'Wrong usage!'

    num1 = float(request.query.num1)
    num2 = float(request.query.num2)

    return str(num1 * num2)


# multiply any number of numbers
# 1. get url
# 2. get query parameters
# 3. post


@route('/multi/<numbers_str>')
def multi_multi(number_str):
    numbers = number_str.split(',')





run(host='localhost', port=8080, debug=True)
