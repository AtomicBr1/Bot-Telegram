import requests
import time

start_time = time.time()

url = 'https://chat.openai.com/'

try:
    response = requests.get(url)
    response.raise_for_status()  # Verificar se houve algum erro na requisição

    html = response.text  # HTML da página

    # Faça o que precisar com o HTML aqui
    print(html)

except requests.HTTPError as err:
    print(f'Erro HTTP: {err}')
except requests.RequestException as err:
    print(f'Erro na requisição: {err}')

end_time = time.time()
execution_time = end_time - start_time
print(f"Tempo de execução: {execution_time} segundos")