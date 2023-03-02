import requests
import json

codigo = input('Qual codigo de rastreio: ')

#user = 'YOUR-EMAIL'
#token = 'TOKEN-HERE'
#codigo = 'CODE'


url = "https://api.linketrack.com/track/json?user=luana.lac93@gmail.com&token=c90fdd7aab87afecf4910e3f86764901f2bfaa1d408ab6a6376efd249df801f4&codigo={}".format(codigo)

payload = {}
headers = {}

response = requests.get(url, headers=headers, data = payload)

pacote = response.json()
print(pacote)



listando = pacote.get('eventos')

print('-------------------')
print(pacote['codigo'])
print('-------------------')
print('-------------------')
print(pacote['eventos'])
print('-------------------')
print('-------------------')
print(list(listando))
