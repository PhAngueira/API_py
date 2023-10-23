import requests

cep = "01.310-100"
cep = cep.replace(".","").replace("-","")
print(f'cep:{cep}')
if len(cep) == 8:
    url = f"https://viacep.com.br/ws/{cep}/json/"

    requisicao = requests.get(url)

    dic_requisicao = requisicao.json()
    print(dic_requisicao)
    uf = dic_requisicao['uf']
    cidade = dic_requisicao['localidade']
    ddd = dic_requisicao['ddd']
    print(f'Cidade: {cidade}')
    print(f'UF: {uf}')
    print(f'DDD: {ddd}')
else:
    print('CEP invalido!')