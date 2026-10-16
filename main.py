import requests

def consultar_clima(cidade, api_key):
    # URL base da OpenWeatherMap para busca por nome da cidade
    url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&units=metric&lang=pt_br"
    
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()  

        
        dados = resposta.json()
        
        temp = dados['main']['temp']
        descricao = dados['weather'][0]['description']
        umidade = dados['main']['humidity']
        
        print(f"\n--- Clima em {cidade.title()} ---")
        print(f"Temperatura: {temp}°C")
        print(f"Condição: {descricao.capitalize()}")
        print(f"Umidade: {umidade}%")
        
    except requests.exceptions.HTTPError:
        print("\n[Erro] Cidade não encontrada. Verifique o nome digitado.")
    except requests.exceptions.RequestException as e:
        print(f"\n[Erro de conexão]: {e}")

if __name__ == "__main__":
    API_KEY = "4100a4527a122dfea594effbd5751eb0"  
    
    cidade_usuario = input("Digite o nome da cidade: ")
    if cidade_usuario.strip():
        consultar_clima(cidade_usuario, API_KEY)
    else:
        print("Nome de cidade inválido.")