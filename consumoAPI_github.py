import requests 

print(' ** Github Users **')

username = input('Usuário: ')

url = f'https://api/github.com/user/{username}'

response = requests.get(url)
data = response.json()

print(data)

if response.status_code == 200:
    print(data)
    print('===============================')
    print(f'Nome: {data["name"]}')
    print(f'Bio: {data["bio"]}')
    print(f'Cidade: {data["location"]}')
    print(f'Followers: {data["followers"]}')
    print(f'Following: {data["following"]}')
else:
    print('Usuário não encontrado!')
    