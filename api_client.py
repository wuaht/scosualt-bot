import requests
from helpers import get_args

class APIClient():
    def __init__(self):
        self.url = 'https://api.scosu.net/v1'
    def get_clears(self, arg):

        args = get_args(arg)
        try:
            mode = int(args.get('-mode'))
        except:
            mode = args.get('-mode')
        mode_url = ''
        try:
            length = int(args.get('-l') or args.get('-length'))
        except:
            length = args.get('-l') or args.get('-length')
        length_url = ''

        if isinstance(mode, int):
            if mode != 0 and mode > 0 and mode < 9 and mode != 7:
                mode_url = f'mode={mode}'
        if isinstance(length, int):
            if length != 10 and length > 0 and length < 51:
                length_url = f'user_limit={length}'

        api_url = f'{self.url}/get_clears/'
        if mode_url != '':
            if api_url.__contains__('?'):
                api_url = api_url + '&' + mode_url
            else:
                api_url = api_url + '?' + mode_url
        if length_url != '':
            if api_url.__contains__('?'):
                api_url = api_url + '&' + length_url
            else:
                api_url = api_url + '?' + length_url

        response = requests.get(api_url)
        return response, mode

