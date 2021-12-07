# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import json

import requests
from selectolax.parser import HTMLParser

url = 'https://www.bayut.com/for-sale/property/dubai/'
res = requests.get(url)
html = res.text
tree = HTMLParser(html)
sep = '}}'


def main():
    script = tree.css('li[aria-label="Listing"]')
    string: str = ''
    for key, value in enumerate(script):
        key = '"' + key.__str__() + '":'
        value = value.text()

        value = value.split(sep, 1)[0]
        value = value + '},'
        value = value + '"price":' + prices()
        value = value + '"location":' + locations()
        value = value + '"beds":' + bed()
        value = value + '"baths":' + bath()
        value = value + '"area":' + areas()
        value = value + '},'
        value = key + value
        value = value[0:-1]
        string += value + ','
    string = string[0:-1]
    string = '{' + string + '}'

    data = json.loads(string)

    with open('script.json', "w", encoding='utf-8') as file:
        json.dump(data, file)


def prices():
    price = tree.css('span[aria-label="Price"]')
    for key, value in enumerate(price):
        value = '"' + value.text() + '",'

        return value


def locations():
    location = tree.css('div[aria-label="Location"]')
    for key, value in enumerate(location):
        value = '"' + value.text() + '",'
        return value


def bed():
    beds = tree.css('span[aria-label="Beds"]')
    for key, value in enumerate(beds):
        value = '"' + value.text() + '",'
        return value


def bath():
    baths = tree.css('span[aria-label="Baths"]')
    for key, value in enumerate(baths):
        value = '"' + value.text() + '",'
        return value


def areas():
    area = tree.css('span[aria-label="Area"]')
    for key, value in enumerate(area):
        value = value.text()
        value = '"' + value[0:-4] + '"'
        return value

    # script = tree.css_first('li[aria-label="Listing"]').text()
    # script = script.split(sep, 1)[0]
    # script = script + '},'
    # price = '"' + tree.css_first('span[aria-label="Price"]').text() + '",'
    # location = '"' + tree.css_first('div[aria-label="Location"]').text() + '",'
    # beds = '"' + tree.css_first('span[aria-label="Beds"]').text() + '",'
    # baths = '"' + tree.css_first('span[aria-label="Baths"]').text() + '",'
    # area = tree.css_first('span[aria-label="Area"]').text() + '",'
    # area = '"' + area[0:-6] + '"'
    # script = script + '"price":' + price
    # script = script + '"location":' + location
    # script = script + '"beds":' + beds
    # script = script + '"baths":' + baths
    # script = script + '"area":' + area
    # script = script + '}'
    #
    # data = json.loads(script)
    #
    # with open('script.json', "w", encoding='utf-8') as file:
    #     json.dump(data, file)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
