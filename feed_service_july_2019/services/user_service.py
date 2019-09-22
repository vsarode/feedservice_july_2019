import json

import requests

def get_user_data_from_user_service(token):
    url = 'http://localhost/userservice/login/' + token
    response = requests.get(url)
    print response
    if response.status_code!=200:
        raise Exception
    return response.json()


if __name__ == '__main__':
    print get_user_data_from_user_service("f49e8115-5512-4b4f-be50-055a0f0c5e87")
