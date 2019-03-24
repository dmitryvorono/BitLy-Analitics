import requests
import os
from dotenv import load_dotenv
import argparse


def get_headers(token):
    authorization_template = 'Bearer {}'
    return {
        'Authorization': authorization_template.format(token),
        'Content-Type': 'application/json'
    }


def reduce_link(url, token):
    data = {'long_url': url}
    response = requests.post(
        'https://api-ssl.bitly.com/v4/shorten',
        headers=get_headers(token),
        json=data)
    if not response.ok:
        return None
    response_json = response.json()
    return response_json['link']


def get_click_count(bitlink, token):
    api_template = 'https://api-ssl.bitly.com/v4/bitlinks/{}/clicks/summary'
    params = {
        'unit': 'day',
        'units': -1,
    }
    response = requests.get(
        api_template.format(bitlink),
        headers=get_headers(token),
        params=params)
    if not response.ok:
        return None
    response_json = response.json()
    return response_json['total_clicks']


def is_bitlink(url, token):
    api_template = 'https://api-ssl.bitly.com/v4/bitlinks/{}'
    params = {
        'unit': 'day',
        'units': -1,
    }
    response = requests.get(
        api_template.format(url), headers=get_headers(token), params=params)
    return response.ok


def main():
    load_dotenv()
    parser = argparse.ArgumentParser(
        description='This programm generate or check bitly links'
    )
    parser.add_argument('link', help='Link or bitly link')
    args = parser.parse_args()
    url = args.link
    token = os.getenv('TOKEN')
    if is_bitlink(url, token):
        print_value = get_click_count(url, token)
    else:
        print_value = reduce_link(url, token)
    print('Link is incorrect' if print_value is None else print_value)


if __name__ == '__main__':
    main()
