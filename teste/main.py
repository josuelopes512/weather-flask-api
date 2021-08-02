import requests

def index(url):
    req = requests.get(url)
    if req.status_code == 200:
        return 'Status OK'
    else:
        raise 'ERRO'


if __name__ == '__main__':
    site = input('Digite um Site: ')
    print(site)
    print(index(site))