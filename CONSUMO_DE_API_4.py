import requests
url = ' https://viacep.com.br/abc/'
cep = '30140071'
formato = '/json/'
r = requests.get(url + cep + formato)
if (r.status_code == 200):
    print()
    print('JSON : ', r.json)
    print()
else:
    print(r.status_code)
    print('Nao houve sucesso na requisicao.')
    print(r.text)