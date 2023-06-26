import requests

# URL de exemplo
url = 'https://geoex.com.br/'

# Enviar uma requisição GET
response = requests.get(url)

# Obter o cabeçalho da resposta
header = response.headers

# Exibir o cabeçalho completo
print(header)

# Verificar se há cookies no cabeçalho
if 'Set-Cookie' in header:
    print("Cookies encontrados:")
    cookies = header['Set-Cookie'].split(';')
    for cookie in cookies:
        print(cookie.strip())
else:
    print("Nenhum cookie encontrado na resposta.")
