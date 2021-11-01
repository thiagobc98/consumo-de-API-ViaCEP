import requests
url = 'https://viacep.com.br/ws/'
listaceps = ['30140071','30140072', '30140073', '30140074',
'30140075','30140076']
formato = '/xml/'
for cep in listaceps:
    r = requests.get(url + cep + formato)
    if (r.status_code == 200):
        print()
        print('CEP : ', cep)
        print('XML : ', r.text)
        print()
    else:
        print('Nao houve sucesso na requisicao.')