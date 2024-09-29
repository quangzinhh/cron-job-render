import requests
import time

def call_api():
    url = 'https://your-api-endpoint.com'
    response = requests.get(url)
    print(f'API response: {response.status_code}, {response.text}')

if __name__ == '__main__':
    while True:
        call_api()
        time.sleep(30)