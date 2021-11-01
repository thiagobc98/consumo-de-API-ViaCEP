import requests
url = 'https://viacep.com.br/ws/'
cep = '30140071'
formato = '/xml/'
r = requests.get(url + cep + formato)
if (r.status_code == 200):
    print()
    print('XML : ', r.text)
    print()
else:
    print('Nao houve sucesso na requisicao.')

