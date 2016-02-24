from bottle import request, route, run


@route('/multi2/<num1>/<num2>')  # /multi2/5.2/3.4
@route('/multi2/<num1>,<num2>')  # /multi2/5.2,3.4
def multiply(num1, num2):
    num1 = float(num1)
    num2 = float(num2)

    return str(num1 * num2)


# query parameters
@route('/multi2')  # /multi2?num1=12&num2=24
def multi_query():
    if 'num1' not in request.query or \
       'num2' not in request.query:  # dict
        return 'Wrong usage!'

    num1 = float(request.query.num1)  # property
    num2 = float(request.query.num2)

    return str(num1 * num2)


# multiply any number of numbers
# 3. post


# get url
@route('/multimulti/<numbers_str>')  # /multimulti/3,5,7,9,11,13,15,17,19
def multi_multi(numbers_str):
    numbers = numbers_str.split(',')

    m = 1
    for number in numbers:
        m *= float(number)

    return str(m)


# get query parameters
@route('/multimulti')  # /multimulti?n1=3&n2=5&n3=7
def multi_multi_query():
    keys = request.query.keys()

    m = 1
    for key in keys:
        number = float(request.query[key])
        m *= number

    return str(m)


# post multi multi


run(host='localhost', port=8080, debug=True)
