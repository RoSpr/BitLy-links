from dotenv import load_dotenv
import argparse
import os
import requests


def is_bitlink(token, link):
    if link.startswith("http://"):
        link = link.replace("http://", "")
    elif link.startswith("https://"):
        link = link.replace("https://", "")

    url = 'https://api-ssl.bitly.com/v4/bitlinks/{}'.format(link)

    headers = {
        "Authorization": ACCESS_TOKEN
    }

    response = requests.get(url, headers=headers)

    return response.ok


def shorten_the_link(token, link):
    url = 'https://api-ssl.bitly.com/v4/bitlinks'

    headers = {
        "Authorization": token
    }

    payload = {
        "long_url": link
    }

    response = requests.post(url, headers=headers, json=payload)

    response.raise_for_status()

    bitlink = response.json()['id']
    return bitlink


def count_clicks(token, link):
    url = 'https://api-ssl.bitly.com/v4/bitlinks/{}/clicks/summary'.format(link)

    headers = {
        "Authorization": token
    }

    response = requests.get(url, headers=headers)

    response.raise_for_status()

    statistics = response.json()['total_clicks']
    return statistics


if __name__ == "__main__":
    load_dotenv()
    ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")

    parser = argparse.ArgumentParser()
    parser.add_argument("link", help="creates a  bitlink if standard link is given (e.g. 'http://google.com');"
                                     "displays sum of link clicks if bitlink is given (e.g 'bit.ly/2ZHJWq4')", type=str)
    args = parser.parse_args()

    link = args.link

    bitlink_test = is_bitlink(ACCESS_TOKEN, link)

    if bitlink_test is True:
        if link.startswith("http://"):
            newlink = link.replace("http://", "")
            try:
                statistics = count_clicks(ACCESS_TOKEN, newlink)
                print("Количество переходов по ссылке {}: {}".format(link, statistics))
            except requests.exceptions.HTTPError as error:
                print("Ошибка: {}".format(error))

        elif link.startswith("https://"):
            newlink = link.replace("https://", "")
            try:
                statistics = count_clicks(ACCESS_TOKEN, newlink)
                print("Количество переходов по ссылке {}: {}".format(link, statistics))
            except requests.exceptions.HTTPError as error:
                print("Ошибка: {}".format(error))

        else:
            try:
                statistics = count_clicks(ACCESS_TOKEN, link)
                print("Количество переходов по ссылке {}: {}".format(link, statistics))
            except requests.exceptions.HTTPError as error:
                print("Ошибка: {}".format(error))

    elif link.startswith("http://") or link.startswith("https://"):
        try:
            bitlink = shorten_the_link(ACCESS_TOKEN, link)
            print("Сокращённая ссылка: ", bitlink)
        except requests.exceptions.HTTPError as error:
            print("Ошибка: {}".format(error))

    else:
        print("Ссылка введена неверно")
