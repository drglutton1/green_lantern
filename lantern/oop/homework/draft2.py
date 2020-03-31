import requests


def return_1_fun():
    return 1


def return_boolean_value(n):
    if n % 2 == 0:
        return True


def call_to_different_service():
    resp = requests.get("http://www.apple.com")
    return resp


call_to_different_service()


def parse_response():
    data = call_to_different_service()
    if data:
        return "OK"


print(parse_response())


def raise_an_error():
    raise ValueError

