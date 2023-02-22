import ast

import arguing
import requests
from bs4 import BeautifulSoup

dict_params = {
    'method': 'get',
    'headers': {
        'User-Agent': 'CScrape/1.0.0'
    }
}


def main():
    url = arguing.set('--url', required=True, help='URL to scrape.')
    params = arguing.set('--params', help='Dict-formatted parameters.', default='{}')
    oneline = arguing.set('--oneliner', help='Oneliner to eval.', default='nodes')
    selector = arguing.set('--select', help='CSS Selector.', default='*')

    dict_params.update(ast.literal_eval(params))

    request = requests.request(url=url, **dict_params)
    soup = BeautifulSoup(request.text, 'lxml')
    tags = soup.select(selector)

    print(eval(oneline, {'nodes': tags}))


if __name__ == '__main__':
    main()
